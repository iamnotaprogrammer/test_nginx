import os
import argparse
import gen_string
# proxy_cache_path /home/ivan/cache1 levels=1:2 keys_zone=hotelbook:800m inactive=1d max_size=30g;
# proxy_cache_path /home/ivan/cache2 levels=1:2 keys_zone=sberbank:800m inactive=1d max_size=30g;
# proxy_cache_path /home/ivan/cache3 levels=1:2 keys_zone=kfc:800m
# inactive=1d max_size=30g


def get_proxy_cache_path(path, max_size='1g', key_zone_size='100m'):
    key_zone = gen_string.random_string(10)
    key_zone += ":"+str(key_zone_size)
    print path
    template = "proxy_cache_path <path> levels=1:2 keys_zone=<key_zone> inactive=1d max_size=<max_size>;"
    return template.replace('<path>', path).replace('<key_zone>',key_zone).replace('<max_size>', max_size)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Process create nginx configurations (in current directory)')
    parser.add_argument('--path', help='dir the top of all cache dirs', default='/home/test/')
    parser.add_argument('--name', help='name of config', default='test.conf')
    parser.add_argument('--template_path',help='path to nginx template config', default=os.path.dirname(os.path.abspath(__file__))+'/template.conf')
    parser.add_argument('--max_size', default='1g' ,
                        help='path to nginx template config')

    args = parser.parse_args()
    path = args.path
    name = args.name
    template_path = args.template_path
    max_size = args.max_size
    current_dir = os.path.dirname(os.path.abspath(__file__))+'/'

    cache_dirs = [x[0] for x in os.walk(path) if x[0] != path]

    with open(template_path, 'rw') as template:
        with open(current_dir + name, 'w') as config:
            for line in template:
                if '<proxy_cache_path>' in line:
                    for el in cache_dirs:
                        config.write('\t')
                        config.write(get_proxy_cache_path(el))
                        config.write('\n')
                else:
                    config.write(line)
    print 'Create {} proxy_cache_path lines'.format(len(cache_dirs))