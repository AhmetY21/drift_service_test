def load_config(file_path='config/config.txt'):
    config = {}
    with open(file_path, 'r') as file:
        for line in file.readlines():
            if '=' not in line:
                continue
            key, value = map(str.strip, line.strip().split('=', 1))
            config[key] = [v.strip() for v in value.split(',')] if ',' in value else value.strip()

    # Parse thresholds
    thresholds = {}
    for key, value in config.items():
        parts = key.rsplit('_', 2)
        if len(parts) == 3:
            test, level = parts[0], parts[2]
            thresholds.setdefault(test, {})[level] = float(value)
    config['THRESHOLDS'] = thresholds
    
    return config
