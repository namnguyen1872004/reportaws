#!/usr/bin/env python3
"""Fix missing images in EN versions by matching sections by NUMBER (5.3.1, etc.)"""
import re

PAIRS = [
    ('content/5-Workshop/5.5/_index.md', 'content/5-Workshop/5.5/_index.vi.md'),
    ('content/5-Workshop/5.6/_index.md', 'content/5-Workshop/5.6/_index.vi.md'),
    ('content/5-Workshop/5.7/_index.md', 'content/5-Workshop/5.7/_index.vi.md'),
    ('content/5-Workshop/5.8/_index.md', 'content/5-Workshop/5.8/_index.vi.md'),
    ('content/5-Workshop/5.9/_index.md', 'content/5-Workshop/5.9/_index.vi.md'),
]

IMG_PATTERN = re.compile(r'(!\[[^\]]*\]\([^)]+\))')
SECTION_RE = re.compile(r'^(5\.\d+\.\d+\.)')

def read_file(path):
    with open(path, 'rb') as f:
        data = f.read()
    bom = b''
    if data.startswith(b'\xef\xbb\xbf'):
        bom = b'\xef\xbb\xbf'
        data = data[3:]
    if b'\r\n' in data:
        eol = '\r\n'
    else:
        eol = '\n'
    text = data.decode('utf-8')
    return bom, eol, text

def write_file(path, bom, eol, text):
    with open(path, 'wb') as f:
        f.write(bom)
        f.write(text.encode('utf-8'))

def get_section_starts(text):
    """Return list of (line_index, section_number) for each section start.
    A section start is a line beginning with '5.X.Y.'.
    """
    lines = text.split('\n')
    starts = []
    for i, line in enumerate(lines):
        m = SECTION_RE.match(line.strip())
        if m:
            starts.append((i, m.group(1)))
    return starts, lines

def process_pair(en_path, vi_path):
    print(f'\n=== Processing {en_path} ===')
    en_bom, en_eol, en_text = read_file(en_path)
    vi_bom, vi_eol, vi_text = read_file(vi_path)
    
    en_starts, en_lines = get_section_starts(en_text)
    vi_starts, vi_lines = get_section_starts(vi_text)
    
    # Build map: section_number -> (start_line_idx, end_line_idx) in lines list
    en_sections = {}
    for i, (start, num) in enumerate(en_starts):
        end = en_starts[i+1][0] if i+1 < len(en_starts) else len(en_lines)
        en_sections[num] = (start, end)
    
    vi_sections = {}
    for i, (start, num) in enumerate(vi_starts):
        end = vi_starts[i+1][0] if i+1 < len(vi_starts) else len(vi_lines)
        vi_sections[num] = (start, end)
    
    # For each section, count images in EN vs VI
    # Then for sections where VI has more images, find the non-image lines in VI section
    # and use them as anchors to insert images into EN section
    
    # Build new EN lines
    new_en_lines = list(en_lines)
    insertions = []  # (insert_position, img_line) - in reverse order
    
    for num in en_sections:
        if num not in vi_sections:
            continue
        en_start, en_end = en_sections[num]
        vi_start, vi_end = vi_sections[num]
        
        # Get non-image lines in VI section (anchors)
        vi_section_lines = vi_lines[vi_start:vi_end]
        en_section_lines = en_lines[en_start:en_end]
        
        vi_img_count = sum(1 for l in vi_section_lines if IMG_PATTERN.search(l))
        en_img_count = sum(1 for l in en_section_lines if IMG_PATTERN.search(l))
        
        if vi_img_count <= en_img_count:
            continue
        
        # Walk through VI section; for each non-image line, find matching line in EN section
        # and track position. For each image line, add to insertions list.
        en_pos = en_start  # current position in new_en_lines (relative to original)
        
        # We need to track position as we walk. Since insertions modify indices,
        # we collect insertion plan first then apply.
        local_inserts = []  # (relative_pos_from_en_start, img_line)
        en_pos_local = 0  # relative position in EN section
        
        for vi_line in vi_section_lines:
            if IMG_PATTERN.search(vi_line):
                # Insert this image at en_pos_local
                local_inserts.append((en_pos_local, vi_line))
            else:
                # Find this non-image line in EN section starting from en_pos_local
                vi_stripped = vi_line.strip()
                if not vi_stripped:
                    continue  # skip empty lines
                found = False
                for k in range(en_pos_local, len(en_section_lines)):
                    if not IMG_PATTERN.search(en_section_lines[k]):
                        if en_section_lines[k].strip() == vi_stripped:
                            en_pos_local = k + 1
                            found = True
                            break
                # If not found, keep position the same
        
        # Add insertions to global list (adjusting positions)
        for rel_pos, img_line in local_inserts:
            global_pos = en_start + rel_pos
            insertions.append((global_pos, img_line))
    
    # Sort insertions in reverse order (insert from end to start)
    insertions.sort(key=lambda x: -x[0])
    
    # Check for duplicates at same position
    seen_positions = {}
    for pos, line in insertions:
        if pos not in seen_positions:
            seen_positions[pos] = []
        seen_positions[pos].append(line)
    
    for pos, line in insertions:
        new_en_lines.insert(pos, line)
    
    new_text = '\n'.join(new_en_lines)
    
    if new_text != en_text:
        write_file(en_path, en_bom, en_eol, new_text)
        print(f'  -> Updated {en_path} with {len(insertions)} image insertions')
    else:
        print(f'  -> No changes')

if __name__ == '__main__':
    for en_path, vi_path in PAIRS:
        process_pair(en_path, vi_path)
    print('\nDone!')
