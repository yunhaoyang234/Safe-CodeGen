def process_code(tree, layer):
    if tree[0] < 257:
        return [[layer] + [tree[1]]]
    processed = []
    layer = layer + 1 if len(tree)>2 else layer
    for t in tree[1:]:
        processed += process_code(t, layer)
    return processed

def extract_words(tree, words):
    extracted = []
    for t in tree:
        if t[1] in words:
            extracted.append(t)
    return extracted

def prev_layer_cond(words, action_idx):
    current = words[action_idx][0]
    conditions = set()
    idx = action_idx
    while idx >= 0:
        idx -= 1
        if words[idx][1] == ':' and current > words[idx][0] + 1:
            current = words[idx][0]
            idx -= 1
            cond = []
            if words[idx][1] == 'else':
                start = 0
                while words[start][1] != 'if':
                    start += 1
                if_idx = start
                while start < idx:
                    while words[start][1] not in ['if', 'elif', 'else']:
                        start += 1
                    cond = []
                    start += 1
                    while words[start][1] != ':':
                        cond.append(words[start][1])
                        start += 1
                    if len(cond) > 0:
                        conditions.add('not (' + ' '.join(cond) + ')')
                idx = if_idx
            else:
                while words[idx][0] != current and idx >= 0:
                    cond.append(words[idx][1])
                    idx -= 1
                cond.reverse()
                if len(cond) == 0:
                    cond = ['True']
                conditions.add(' '.join(cond))
    return conditions

def extract_conditions(action, words):
    conditions = []
    for i in range(len(words)):
        if words[i][1] == action:
            cond = prev_layer_cond(words, i)
            cond_str = []
            for c in cond:
                cond_str.append('('+c+')')
            cond_str_ = ' and '.join(cond_str)
            conditions.append(cond_str_)
    return ' or '.join(conditions)