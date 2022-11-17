def crop(crop_name):
    crop_data = {
    "wheat":["/static/images/wheat.jpg", "Nouga, bogura, dinajpur, CapaiNawabgong, rajshahi, natore ", "rabi","Sri Lanka, United Arab Emirates, Taiwan"],
    "paddy":["/static/images/paddy.jpg", "mymensingh, Nouga,  Khulna, bhola, T.N.", "kharif","Bangladesh, Saudi Arabia, Iran"],
    "barley":["/static/images/barley.jpg", "coxbazar, Uttar Khulna,  Khulna, Rajshahi, bhola", "rabi","Oman, UK, Qatar, USA"],
    "maize":["/static/images/maize.jpg", "dinajpur, bogura, rajshahi, rongpur, ponchogor", "kharif", "Hong Kong, United Arab Emirates, France"],
    "bajra":["/static/images/bajra.jpg", "coxbazar, bhola, Rajshahi, Uttar Khulna and rajshahi", "kharif", "Oman, Saudi Arabia, Israel, Japan"],
    "copra":["/static/images/copra.jpg", "nilphamari, Bagerhat, faridpur,  Khulna, khulna, Gopalgong","rabi", "Veitnam, Bangladesh, Iran, Malaysia"],
    "cotton":["/static/images/cotton.jpg", "bhola, Rajshahi, rangamati, Bagerhat,  Khulna, rajshahi", " China, Bangladesh, Egypt"],
    "masoor":["/static/images/masoor.jpg", "Uttar Khulna,  Khulna, chandpur, Gopalgong, coxbazar", "rabi", "Pakistan, Cyprus,United Arab Emirates"],
    "gram":["/static/images/gram.jpg", "rajshahi, dhaka, madaripur, kushtia, borishal", "rabi", "Veitnam, Spain, Myanmar"],
    "groundnut":["/static/images/groundnut.jpg", " Khulna, rajshahi, Bagerhat, faridpur, and rangamati", "kharif", "Indonesia, Jordan, Iraq"],
    "arhar":["/static/images/arhar.jpg", "rangamati, faridpur,  Khulna and  Khulna", "kharif", "United Arab Emirates, USA, Chicago"],
    "sesamum":["/static/images/sesamum.jpg", "faridpur, gopalgong, shoriyotpur, feni, satkhira", "rabi", "Iraq, South Africa, USA, Netherlands"],
    "jowar":["/static/images/jowar.jpg", "rangamati, faridpur,  Khulna,  Khulna, rajshahi", "kharif", "Torronto, Sydney, New York"],
    "moong":["/static/images/moong.jpeg", "moulovibazar, dhaka, chandpur,kishorgong,faridpur", "rabi", "Qatar, United States, Canada"],
    "niger":["/static/images/niger.jpg", " Khulna, Assam, Chattisgarh, rajshahi, Jharkhand", "kharif", "United States of American,Argenyina, Belgium"],
    "rape":["/static/images/rape.jpg", "dinajpur, bogura, rajshahi, rongpur, ponchogor,nilfamari,kurigram","rabi", "Veitnam, Malaysia, Taiwan"],
    "jute":["/static/images/jute.jpg", " faridpur , comilla , mymensingh , pabna , jessore", "kharif", "JOrdan, United Arab Emirates, Taiwan"],
    "safflower":["/static/images/safflower.jpg",  "rangamati, faridpur,  Khulna,  Khulna, khulna", "kharif", " Philippines, Taiwan, Portugal"],
    "soyabean":["/static/images/soyabean.jpg",  " Khulna, rangamati, coxbazar,  Khulna and rangamati", "kharif", "Spain, Thailand, Singapore"],
    "urad":["/static/images/urad.jpg",  " Khulna, bhola,  Khulna, Bagerhat", "rabi", "United States, Canada, United Arab Emirates"],
    "ragi":["/static/images/ragi.jpg",  "bhola, Bagerhat and Uttarakhand", "kharif", "United Arab Emirates, New Zealand, Bahrain"],
    "sunflower":["/static/images/sunflower.jpg",  "faridpur,  Khulna, bhola, chandpur, khulna", "rabi", "Phillippines, United States, Bangladesh"],
    "sugarcane":["/static/images/sugarcane.jpg","rajshahi, pabna, CapaiNawabgong, joypurhat, natore" , "kharif", "Kenya, United Arab Emirates, United Kingdom"]
    }
    return crop_data[crop_name]