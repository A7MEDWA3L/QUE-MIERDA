print("The first number must be in uppercase.")
while True:
    country = input("Enter your country:    -")

    very_poor = ["Burundi", "Somalia", "Mozambique", "Central African Republic", "Madagascar", "Sierra Leone", "Afghanistan", "Democratic Congo", "Niger", "Eritrea", "Malawi", "Liberia", "Equatorial Guinea", "Yemen", "Chad", "Sudan", "Guinea Bissau", "Rwanda", "Gambia", "Uganda", "Tajikistan", "Mali", "Burkina Faso", "Ethiopia", "Togo", "South Sudan", "Zambia", "Tanzania", "Lesotho",  	"Guinea", 	"Myanmar", 	"Nepal", "Syrian Arab Republic","Kyrgyzstan","Benin", "Timor Leste", "Comoros","Kiribati", "Pakistan","Cambodia","Senegal","Cameroon","Mauritania","Zimbabwe", "Haiti", "Uzbekistan",		"Kenya", "Nigeria","Nicaragua", "Angola", "Congo","India", "Solomon Islands", "Ghana", "Sao Tome and Principe", "Bangladesh", "Lao PDR", "Ivory coast", "Lebanon", "Iran", "Honduras", "Papua New Guinea", "Bhutan", "Vanuatu", "Djibouti", "Bolivia", "Cape verde"]
    if country in very_poor:
        print("This country is very poor :")

    poor=["Micronesia","Morocco","Philippines","Palestine","Vietnam","Algeria","Sri Lanka","Egypt","Tunisia","Samoa","Marshall Islands","Eswatini","Indonesia","Jordan","El Salvador","Belize","Mongolia","Jamaica","Tonga","Armenia","Namibia","Ukraine","Suriname","Kosovo","Guatemala","Georgia","Iraq","Fiji","Tuvalu","Moldova","zerbaijan","Paraguay","Ecuador","Libya","Colombia","Albania","Peru","North Macedonia","Bosnia","Herzegovina","South Africa","Thailand","Belarus","Botswana","Brazil","Dominica,""Turkmenistan","Saint Vincent","the Grenadines","Gabon","Dominican Republic","Mauritius","Maldives",]
    if country in poor:
        print("This country is poor")

    rich = ["Serbia","Montenegro","Guyana","Cuba","Saint Lucia","Turkiye","Mexico","Grenada","Kazakhstan","Argentina","Malaysia","Bulgaria","Russia","Nauru","Costa Rica","China","American Samoa","Seychelles","Palau","Panama","Romania","Antigua Barbuda","Trinidad","obago","Venezuela","Curacao","Oman","Chile","Uruguay","Barbados","Croatia","Poland","Saint Kitts","Nevis","Hungary","French Polynesia","Greece","Latvia","Northern Mariana Islands","Slovakia","Saint Martin","Bahrain","Aruba","Lithuania","Saudi Arabia","Turks","Caicos Islands","Portugal","Kuwait"]

    if country in rich:
        print("This country is rich")

    very_rich = ["Czechia","Estonia","Bahamas","Dutch Saint Martin","Slovenia","Spain","cyprus","Puerto Rico","Brunei","Maltav","Czechia","Estonia","Bahamas","Dutch Saint Martin","Slovenia","Spain","Cyprus","Puerto Rico","Brunei","Maltav","Guam","North Macedonia","South Korea","Italy","United Arab Emirates","Japan","Virgin Islands","Andorra","France","Macao","San Marino","United Kingdom""New Zealand","Hong Kong""Germany","Belgium","Canada","Austria","Finland","Greenland,""Netherlands,""Australia","Sweden","Qatar","Faroe Islands","Denmark","Iceland","United States","Singapore","Channel Islands","Cayman Islands""Isle of Man","Norway","Switzerland","Ireland","Bermuda","Luxembourg","Liechtenstein","Monaco","Guam","South Korea","Italy","United Arab Emirates","Japan","Virgin Islands","Andorra","France","Macao","San Marino""United Kingdom""New Zealand","Hong Kong""Germany","Belgium","Canada","Austria","Finland","Greenland,""Netherlands,""Australia","Sweden","Qatar","Faroe Islands","Denmark","Iceland","Singapore","Channel Islands","Cayman Islands","Isle of man""Norway","Switzerland","Ireland","Bermuda","Luxembourg","Liechtenstein","Monaco"]
    if country in very_rich:
        print("This country is very rich.")

    print("")