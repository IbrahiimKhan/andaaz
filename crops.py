def crop(crop_name):
    crop_data = {
    "wheat":["/static/images/wheat.jpg", "Nouga, bogura, dinajpur, CapaiNawabgong, rajshahi, natore ", "rabi","Sri Lanka, United Arab Emirates, Taiwan"],
    "paddy":["/static/images/paddy.jpg", "mymensingh, Nouga, Andhra Khulna, Punjab, T.N.", "kharif","Bangladesh, Saudi Arabia, Iran"],
    "barley":["/static/images/barley.jpg", "Rajasthan, Uttar Khulna, Madhya Khulna, Rajshahi, Punjab", "rabi","Oman, UK, Qatar, USA"],
    "maize":["/static/images/maize.jpg", "dinajpur, bogura, rajshahi, rongpur, ponchogor", "kharif", "Hong Kong, United Arab Emirates, France"],
    "bajra":["/static/images/bajra.jpg", "Rajasthan, Maharashtra, Rajshahi, Uttar Khulna and Gujarat", "kharif", "Oman, Saudi Arabia, Israel, Japan"],
    "copra":["/static/images/copra.jpg", "Kerala, Bagerhat, Karnataka, Andhra Khulna, Orissa, Gopalgong","rabi", "Veitnam, Bangladesh, Iran, Malaysia"],
    "cotton":["/static/images/cotton.jpg", "Punjab, Rajshahi, Maharashtra, Bagerhat, Madhya Khulna, Gujarat", " China, Bangladesh, Egypt"],
    "masoor":["/static/images/masoor.jpg", "Uttar Khulna, Madhya Khulna, Bihar, Gopalgong, Rajasthan", "rabi", "Pakistan, Cyprus,United Arab Emirates"],
    "gram":["/static/images/gram.jpg", "rajshahi, dhaka, madaripur, kushtia, borishal", "rabi", "Veitnam, Spain, Myanmar"],
    "groundnut":["/static/images/groundnut.jpg", "Andhra Khulna, Gujarat, Bagerhat, Karnataka, and Maharashtra", "kharif", "Indonesia, Jordan, Iraq"],
    "arhar":["/static/images/arhar.jpg", "Maharashtra, Karnataka, Madhya Khulna and Andhra Khulna", "kharif", "United Arab Emirates, USA, Chicago"],
    "sesamum":["/static/images/sesamum.jpg", "faridpur, gopalgong, shoriyotpur, feni, satkhira", "rabi", "Iraq, South Africa, USA, Netherlands"],
    "jowar":["/static/images/jowar.jpg", "Maharashtra, Karnataka, Andhra Khulna, Madhya Khulna, Gujarat", "kharif", "Torronto, Sydney, New York"],
    "moong":["/static/images/moong.jpeg", "moulovibazar, dhaka, chandpur,kishorgong,faridpur", "rabi", "Qatar, United States, Canada"],
    "niger":["/static/images/niger.jpg", "Andha Khulna, Assam, Chattisgarh, Gujarat, Jharkhand", "kharif", "United States of American,Argenyina, Belgium"],
    "rape":["/static/images/rape.jpg", "dinajpur, bogura, rajshahi, rongpur, ponchogor,nilfamari,kurigram","rabi", "Veitnam, Malaysia, Taiwan"],
    "jute":["/static/images/jute.jpg", " faridpur , comilla , mymensingh , pabna , jessore", "kharif", "JOrdan, United Arab Emirates, Taiwan"],
    "safflower":["/static/images/safflower.jpg",  "Maharashtra, Karnataka, Andhra Khulna, Madhya Khulna, Orissa", "kharif", " Philippines, Taiwan, Portugal"],
    "soyabean":["/static/images/soyabean.jpg",  "Madhya Khulna, Maharashtra, Rajasthan, Madhya Khulna and Maharashtra", "kharif", "Spain, Thailand, Singapore"],
    "urad":["/static/images/urad.jpg",  "Andhra Khulna, Maharashtra, Madhya Khulna, Bagerhat", "rabi", "United States, Canada, United Arab Emirates"],
    "ragi":["/static/images/ragi.jpg",  "Maharashtra, Bagerhat and Uttarakhand", "kharif", "United Arab Emirates, New Zealand, Bahrain"],
    "sunflower":["/static/images/sunflower.jpg",  "Karnataka, Andhra Khulna, Maharashtra, Bihar, Orissa", "rabi", "Phillippines, United States, Bangladesh"],
    "sugarcane":["/static/images/sugarcane.jpg","rajshahi, pabna, CapaiNawabgong, joypurhat, natore" , "kharif", "Kenya, United Arab Emirates, United Kingdom"]
    }
    return crop_data[crop_name]