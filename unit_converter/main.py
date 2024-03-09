"""
Author: Justin Myshrall
Date 3/8/2024
"""

from conversions import Converter

conv = Converter()

while True:
    print('Select unit to convert')

    unit = input('in/ft/yd/mi/mm/cm/m/km/exit: ')

    if unit == 'exit':
        print('Quitting program')
        break
    
    if unit == 'in':
        in_choice = input('Select what to convert inches to, ft/yd/mi/mm/cm/m/km: ')
        x = float(input('Enter inches to convert: '))
        print('Result: ', format(conv.imperial_in(in_choice, x), '.2e'))
    
    elif unit == 'ft':
        ft_choice = input('Select what to convert feet to, in/yd/mi/mm/cm/m/km: ')
        x = float(input('Enter feet to convert: '))
        print('Result: ', format(conv.imperial_ft(ft_choice, x), '.2e'))
    
    elif unit == 'yd':
        yd_choice = input('Select what to convert yards to, ft/in/mi/mm/cm/m/km: ')
        x = float(input('Enter yards to convert: '))
        print('Result: ', format(conv.imperial_yd(yd_choice, x), '.2e'))
    
    elif unit == 'mi':
        mi_choice = input('Select what to convert miles to, ft/yd/in/mm/cm/m/km: ')
        x = float(input('Enter miles to convert: '))
        print('Result: ', format(conv.imperial_mi(mi_choice, x), '.2e'))
    
    elif unit == 'mm':
        mm_choice = input('Select what to convert millimeters to, ft/yd/in/mi/cm/m/km: ')
        x = float(input('Enter millimeters to convert: '))
        print('Result: ', format(conv.metric_mm(mm_choice, x), '.2e'))
    
    elif unit == 'cm':
        cm_choice = input('Select what to convert centimeters to, ft/yd/in/mi/mm/cm/m/km: ')
        x = float(input('Enter centimeters to convert: '))
        print('Result: ', format(conv.metric_cm(cm_choice, x), '.2e'))
    
    elif unit == 'm':
        m_choice = input('Select what to convert meters to, ft/yd/in/mi/mm/cm/km: ')
        x = float(input('Enter meters to convert: '))
        print('Result: ', format(conv.metric_m(m_choice, x), '.2e'))
    
    elif unit == 'km':
        km_choice = input('Select what to convert kilometers to, ft/yd/in/mi/mm/cm/m/km: ')
        x = float(input('Enter kilometers to convert: '))
        print('Result: ', format(conv.metric_km(km_choice, x), '.2e'))
    
    else:
        print('Invalid input. Please select a valid unit.')
        continue 