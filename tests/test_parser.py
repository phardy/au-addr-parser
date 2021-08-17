from au_address_parser import AbAddressUtility, ShortAddressUtility

def unit_helper(address_cls):
    assert address_cls.address == '2/42-44 Example Street, Stanmore NSW 2048'
    assert address_cls.std_address == '2/42 EXAMPLE ST, STANMORE NSW 2048'
    assert address_cls.address_abbr == '2/42-44 EXAMPLE ST, STANMORE NSW 2048'
    assert address_cls.parsed_addr == {'flat_number_prefix': None,
                                       'flat_number': '2',
                                       'flat_number_suffix': None,
                                       'number_first_prefix': None,
                                       'number_first': '42',
                                       'number_first_suffix': None,
                                       'number_last_prefix': None,
                                       'number_last': '44',
                                       'number_last_suffix': None,
                                       'street_name': 'EXAMPLE',
                                       'street_type_abbr': 'ST',
                                       'street_type': 'STREET',
                                       'street_suffix': None,
                                       'street_suffix_abbr': None,
                                       'locality': 'STANMORE',
                                       'state': 'NSW',
                                       'post': '2048'}

def house_helper(address_cls):
    assert address_cls.std_address == '22 EXAMPLE ST, STANMORE NSW 2048'
    assert address_cls.address_abbr == '22 EXAMPLE ST, STANMORE NSW 2048'
    assert address_cls.parsed_addr == {'flat_number_prefix': None,
                                       'flat_number': None,
                                       'flat_number_suffix': None,
                                       'number_first_prefix': None,
                                       'number_first': '22',
                                       'number_first_suffix': None,
                                       'number_last_prefix': None,
                                       'number_last': None,
                                       'number_last_suffix': None,
                                       'street_name': 'EXAMPLE',
                                       'street_type_abbr': 'ST',
                                       'street_type': 'STREET',
                                       'street_suffix': None,
                                       'street_suffix_abbr': None,
                                       'locality': 'STANMORE',
                                       'state': 'NSW',
                                       'post': '2048'}

def special_helper(address_cls):
    assert address_cls.address == '22 Example Street West, Stanmore NSW 2048'
    assert address_cls.std_address == '22 EXAMPLE ST W, STANMORE NSW 2048'
    assert address_cls.address_abbr == '22 EXAMPLE ST W, STANMORE NSW 2048'
    assert address_cls.parsed_addr == {'flat_number_prefix': None,
                                       'flat_number': None,
                                       'flat_number_suffix': None,
                                       'number_first_prefix': None,
                                       'number_first': '22',
                                       'number_first_suffix': None,
                                       'number_last_prefix': None,
                                       'number_last': None,
                                       'number_last_suffix': None,
                                       'street_name': 'EXAMPLE',
                                       'street_type_abbr': 'ST',
                                       'street_type': 'STREET',
                                       'street_suffix': 'WEST',
                                       'street_suffix_abbr': 'W',
                                       'locality': 'STANMORE',
                                       'state': 'NSW',
                                       'post': '2048'}

def test_pars_unit():
    address_cls = AbAddressUtility(
        'Unit 2 42-44 Example ST, STANMORE,  NSW 2048')
    unit_helper(address_cls)


def test_pars_house():
    address_cls = AbAddressUtility('22 Example ST, STANMORE, NSW 2048')
    assert address_cls.address == '22 Example Street, Stanmore NSW 2048'
    address_cls = AbAddressUtility('22 Example ST STANMORE NSW 2048')
    assert address_cls.address == '22 Example Street, Stanmore NSW 2048'
    address_cls = AbAddressUtility('22 Example ST , STANMORE, NSW 2048')
    assert address_cls.address == '22 Example Street, Stanmore NSW 2048'
    address_cls = AbAddressUtility('22 Example Street, STANMORE, NSW 2048')
    assert address_cls.address == '22 Example Street, Stanmore NSW 2048'
    address_cls = AbAddressUtility('22 Example ST, STANMORE WEST, NSW 2048')
    assert address_cls.address == '22 Example Street, Stanmore West NSW 2048'
    address_cls = AbAddressUtility('22 Example ST, STANMORE, NSW 2048')
    house_helper(address_cls)


def test_pars_special():
    address_cls = AbAddressUtility('22 Example ST west, STANMORE, NSW 2048')
    special_helper(address_cls)

def test_short_unit():
    address_cls = ShortAddressUtility('Unit 2 42-44 Example St',
                                      locality='stanmore', state='NSW',
                                      post='2048')
    unit_helper(address_cls)

def test_short_house():
    address_cls = ShortAddressUtility('22 Example ST',
                                      locality='stanmore', state='NSW',
                                      post='2048')
    house_helper(address_cls)

def test_short_special():
    address_cls = ShortAddressUtility('22 Example ST west',
                                      locality='stanmore', state='NSW',
                                      post='2048')
    special_helper(address_cls)
