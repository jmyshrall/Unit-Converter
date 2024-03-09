"""
Author: Justin Myshrall
Date 3/8/2024
"""
class Converter:
    
    def imperial_in(self, in_choice, x):
        """
        Takes imperial unit, inch and converts to metric and imperial units using math operations
        designed to be more expandable to include additional units
        """
        if in_choice == 'mm':      # in to mm
            result = x * 25.4
            return result
        elif in_choice == 'cm':    # in to cm
            result = x * 2.54
            return result
        elif in_choice == 'm':    # in to m
            if x <= 0:
                return ValueError
            # error handle for ALL division by 0
            result = x / 39.37
            return result
        elif in_choice == 'km':    # in to km
            if x <= 0:
                return ValueError
            result = x / 39370
            return result
        elif in_choice == 'ft':    # in to ft
            if x <= 0:
                return ValueError
            result = x / 12
            return result
        elif in_choice == 'yd':    # in to yd
            if x <= 0:
                return ValueError
            result = x / 36
            return result
        elif in_choice == 'mi':    # in to mi
            if x <= 0:
                return ValueError
            result = x / 63360
            return result
        else:
            return ValueError
    
    def imperial_ft(self, ft_choice, x):
        """
        Takes imperial unit feet and converts to metric and imperial units using math operations
        designed to be more expandable to include additional units
        """
        if ft_choice == 'mm':      # ft to mm
            result = x * 304.8
            return result
        elif ft_choice == 'cm':    # ft to cm
            result = x * 30.48
            return result
        elif ft_choice == 'm':    # ft to m
            if x <= 0:
                return ValueError
            result = x / 3.281
            return result
        elif ft_choice == 'km':    # ft to km
            if x <= 0:
                return ValueError
            result = x / 3281
            return result
        elif ft_choice == 'in':    # ft to in
            result = x * 12
            return result
        elif ft_choice == 'yd':    # ft to yd
            if x <= 0:
                return ValueError
            result = x / 3
            return result
        elif ft_choice == 'mi':    # ft to mi
            if x <= 0:
                return ValueError
            result = x / 5280
            return result
        else:
            return ValueError
    
    def imperial_yd(self, yd_choice, x):
        """
        Takes imperial unit yard and converts to metric and imperial units using math operations
        designed to be more expandable to include additional units
        """
        if yd_choice == 'mm':      # yd to mm
            result = x * 914.4
            return result
        elif yd_choice == 'cm':    # yd to cm
            result = x * 91.44
            return result
        elif yd_choice == 'm':    # yd to m
            if x <= 0:
                return ValueError
            result = x / 1.094
            return result
        elif yd_choice == 'km':    # yd to km
            if x <= 0:
                return ValueError
            result = x / 1094
            return result
        elif yd_choice == 'in':    # yd to in
            if x <= 0:
                return ValueError
            result = x * 36
            return result
        elif yd_choice == 'ft':    # yd to ft
            result = x * 3
            return result
        elif yd_choice == 'mi':    # yd to mi
            if x <= 0:
                return ValueError
            result = x / 1760
            return result
        else:
            return ValueError
        
    def imperial_mi(self, mi_choice, x):
        """
        Takes imperial unit mile and converts to metric and imperial units using math operations
        designed to be more expandable to include additional units
        """
        if mi_choice == 'mm':      # mi to mm
            result = x * 1.609e6
            return result
        elif mi_choice == 'cm':    # mi to cm
            result = x * 1.609e5
            return result
        elif mi_choice == 'm':    # mi to m
            if x <= 0:
                return ValueError
            result = x / 1609
            return result
        elif mi_choice == 'km':    # mi to km
            if x <= 0:
                return ValueError
            result = x / 1.609
            return result
        elif mi_choice == 'in':    # mi to in
            result = x * 63360
            return result
        elif mi_choice == 'ft':    # mi to ft
            result = x * 5280
            return result
        elif mi_choice == 'yd':    # mi to yd
            result = x * 1760
            return result
        else:
            return ValueError

    
    def metric_mm(self, mm_choice, x):
        """
        Takes metric unit milimeter and converts to imperial and metric units
        designed to be continuesly expandable
        """
        if mm_choice == 'in':      # mm to in
            if x <= 0:
                return ValueError
            result = x / 25.4
            return result
        elif mm_choice == 'ft':    # mm to ft 
            if x <= 0:
                return ValueError
            result = x / 304.8
            return result
        elif mm_choice == 'yd':    # mm to yd
            if x <= 0:
                return ValueError
            result = x / 914.4
            return result
        elif mm_choice == 'mi':    # mm to mi
            if x <= 0:
                return ValueError
            result = x / 1.609e6
            return result
        elif mm_choice == 'cm':    # mm to cm
            if x <= 0:
                return ValueError
            result = x / 10
            return result
        elif mm_choice == 'm':    # mm to m
            if x <= 0:
                return ValueError
            result = x / 1e3
            return result
        elif mm_choice == 'km':   # mm to km
            if x <= 0:
                return ValueError
            result = x / 1e6
            return result
        else:
            return ValueError
        
    def metric_cm(self, cm_choice, x):
        """
        Takes metric unit centimeter and converts to imperial and metric units
        designed to be continuesly expandable
        """
        if cm_choice == 'in':      # cm to in
            if x <= 0:
                return ValueError
            result = x / 2.54
            return result
        elif cm_choice == 'ft':    # cm to ft 
            if x <= 0:
                return ValueError
            result = x / 30.48
            return result
        elif cm_choice == 'yd':    # cm to yd
            if x <= 0:
                return ValueError
            result = x / 91.44
            return result
        elif cm_choice == 'mi':    # cm to mi
            if x <= 0:
                return ValueError
            result = x / 1.609e5
            return result
        elif cm_choice == 'mm':    # cm to mm
            result = x * 10
            return result
        elif cm_choice == 'm':    # cm to m
            if x <= 0:
                return ValueError
            result = x / 100
            return result
        elif cm_choice == 'km':    # cm to km
            if x <= 0:
                return ValueError
            result = x / 1e5
            return result
        else:
            return ValueError
    
    def metric_m(self, m_choice, x):
        """
        Takes metric unit meter and converts to imperial and metric units
        designed to be continuesly expandable
        """
        if m_choice == 'in':      # m to in
            result = x * 39.37
            return result
        elif m_choice == 'ft':    # m to ft 
            result = x * 3.281
            return result
        elif m_choice == 'yd':    # m to yd
            result = x * 1.094
            return result
        elif m_choice == 'mi':    # m to mi
            if x <= 0:
                return ValueError
            result = x / 1609
            return result
        elif m_choice == 'mm':    # m to mm
            result = x * 1000
            return result
        elif m_choice == 'cm':    # m to cm
            result = x * 100
            return result
        elif m_choice == 'km':    # m to km
            if x <= 0:
                return ValueError
            result = x / 1e3
            return result
        else:
            return ValueError
    
    def metric_km(self, km_choice, x):
        """
        Takes metric unit kilometer and converts to imperial and metric units
        designed to be continuesly expandable
        """
        if km_choice == 'in':      # km to in
            result = x * 39370
            return result
        elif km_choice == 'ft':    # km to ft 
            result = x * 3281
            return result
        elif km_choice == 'yd':    # km to yd
            result = x * 1094
            return result
        elif km_choice == 'mi':    # km to mi
            if x <= 0:
                return ValueError
            result = x / 1.609
            return result
        elif km_choice == 'mm':    # km to mm
            result = x * 1e6
            return result
        elif km_choice == 'cm':    # km to cm
            result = x * 1e5
            return result
        elif km_choice == 'm':    # km to m
            result = x * 1e3
            return result
        else:
            return ValueError
    