#!/usr/bin/python3

class GMLanHeader29:
    
    def __init__(self, header):
        header_int=int(header,16)
        header_bin=bin(header_int)[2:].zfill(4*len(header))
        self.unused=int(header_bin[0:3],2)
        self.priority=int(header_bin[3:6],2)
        self.arbitration=int(header_bin[6:19],2)
        self.ecu_send_id=int(header_bin[19:32],2)
        
    def get_arbitration_id(self):    
        return self.arbitration
    
    def get_arbitration_id_hex(self):    
        return hex(self.arbitration)
    
    def get_priority(self):
        return self.priority

    def get_priority_hex(self):
        return hex(self.priority)
        
    def get_ecu_sender_id(self):
        return self.ecu_send_id
    
    def get_ecu_sender_id_hex(self):
        return hex(self.ecu_send_id)
    
    def get_unused_bits(self):
        return self.unused
    
    def get_unused_bits_hex(self):
        return hex(self.unused)



