airports = {
    "kadapa": "CDP",
    "kurnool": "KJB",
    "puttaparthi": "PUT",
    "rajahmundry": "RJA",
    "tirupati": "TIR",
    "vijayawada": "VGA",
    "visakhapatnam": "VTZ",
    "daporijo": "DEP",
    "itanagar": "HGI",
    "pasighat": "IXT",
    "tezu": "TEI",
    "ziro": "ZER",
    "dhubri": "RUP",
    "dibrugarh": "DIB",
    "guwahati": "GAU",
    "jorhat": "JRH",
    "north lakhimpur": "IXI",
    "silchar": "IXS",
    "tezpur": "TEZ",
    "darbhanga": "DBR",
    "gaya": "GAY",
    "muzaffarpur": "MZU",
    "patna": "PAT",
    "raipur": "RPR",
    "bilaspur": "PAB",
    "jagdalpur": "JGB",
    "dabolim / goa": "GOI",
    "mopa": "GOX",
    "ahmedabad": "AMD",
    "bhavnagar": "BHU",
    "bhuj": "BHJ",
    "jamnagar": "JGA",
    "junagadh": "IXK",
    "kandla": "IXY",
    "porbandar": "PBD",
    "rajkot": "HSR",
    "rajkot airport": "RAJ",
    "surat": "STV",
    "vadodara": "BDQ",
    "hisar": "HSS",
    "kangra": "DHM",
    "kullu-manali": "KUU",
    "shimla": "SLV",
    "deoghar": "DGH",
    "dhanbad": "DBD",
    "sonari": "IXW",
    "ranchi": "IXR",
    "belgavi": "IXG",
    "ballari": "VDY",
    "bengaluru": "BLR",
    "bidar": "IXX",
    "hubli": "HBX",
    "kalaburagi": "GBI",
    "mangaluru": "IXE",
    "mysuru": "MYQ",
    "shivamogga": "RQY",
    "kannur": "CNN",
    "kochi, ernakulam": "COK",
    "kozhikode / malappuram": "CCJ",
    "thiruvananthapuram": "TRV",
    "bhopal": "BHO",
    "gwalior": "GWL",
    "indore": "IDR",
    "jabalpur": "JLR",
    "khajuraho": "HJR",
    "satna": "TNI",
    "akola": "AKD",
    "aurangabad": "IXU",
    "gondia": "GDB",
    "jalgaon": "JLG",
    "kolhapur": "KLH",
    "latur": "LTU",
    "mumbai": "BOM",
    "nagpur": "NAG",
    "nanded": "NDC",
    "nashik": "ISK",
    "osmanabad": "OMN",
    "pune": "PNQ",
    "ratnagiri": "RTC",
    "shirdi": "SAG",
    "solapur": "SSE",
    "sindhudurg": "SDW",
    "yavatmal": "YTL",
    "imphal": "IMF",
    "shillong": "SHL",
    "lengpui airport": "AJL",
    "dimapur": "DMU",
    "berhampur": "QBM",
    "bhubaneswar": "BBI",
    "jeypore": "PYB",
    "jharsuguda": "JRG",
    "rourkela": "RRK",
    "utkela": "UKE",
    "beas": "VIBS",
    "sri guru ram dass jee international airport": "ATQ",
    "bathinda": "BUP",
    "jalandhar": "AIP",
    "ludhiana": "LUH",
    "pathankot": "IXP",
    "ajmer": "KQH",
    "bikaner": "BKB",
    "jaipur": "JAI",
    "jaisalmer": "JSA",
    "jodhpur": "JDH",
    "kota": "KTU",
    "udaipur": "UDR",
    "gangtok": "PYG",
    "chennai": "MAA", 
    "coimbatore": "CJB",  
    "hosur": "VO95",  
    "madurai": "IXM",  
    "neyveli": "NVY",  
    "salem": "SXV",  
    "thanjavur": "TJV", 
    "thoothukkudi": "TCR",  
    "tiruchirappalli": "TRZ",  
    "vellore": "VOVR",
    "hyderabad": "HYD",  
    "begumpet airport": "BPM",  
    "warangal": "WGC",
    "agartala": "IXA",  
    "kailashahar": "IXH",  
    "kamalpur": "IXQ", 
    "khowai": "IXN",
    "agra": "AGR",  
    "aligarh": "HRH",  
    "ayodhya": "AYJ", 
    "bareilly": "BEK",  
    "gautam buddha nagar": "DXN",
    "ghaziabad": "HDO",
    "gorakhpur": "GOP",  
    "kanpur airport": "KNU", 
    "kushinagar": "KBK", 
    "lucknow": "LKO", 
    "prayagraj": "IXD",  
    "varanasi": "VNS",
    "dehradun": "DED",  
    "pantnagar": "PGH", 
    "pithoragarh": "NNS",
    "balurghat": "RGH",  
    "cooch behar": "COH",  
    "durgapur": "RDP",   
    "netaji subhas chandra bose international airport": "CCU",  
    "malda": "LDA", 
    "siliguri": "IXB",
    "port blair": "IXZ",
    "chandigarh": "IXC",
    "diu": "DIU",
    "delhi": "DEL",
    "jammu": "IXJ",
    "srinagar": "SXR",
    "leh": "IXL",
    "agatti island": "AGX",
    "puducherry": "PNY",
    "pondicherry": "PNY"  
}

def getIataCode(city_name, airports):
    city_name = city_name.lower()
    # Check for exact match first
    if city_name in airports:
        return airports[city_name]
    # Perform partial match if no exact match
    for city, code in airports.items():
        if city_name in city.lower():
            return code
    return "No matching airports found."
