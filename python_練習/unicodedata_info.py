import unicodedata

#將 unicode_name 和 unicode_lookup 合併成 unicode_info，同時顯示字符、名稱和查找結果
def unicode_info(value):
    name = unicodedata.name(value)
    lookup_value = unicodedata.lookup(name)
    print(f'value={value}, name={name}, lookup_value={lookup_value}')
    return name, lookup_value

# 測試不同的 Unicode 表示法
unicode_info('我')
unicode_info('\u6211')
unicode_info('\U00006211')

