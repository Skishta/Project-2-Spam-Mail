                #PROJECT 2 (SPAM_MAIL)
#بطلب من اليوزر يدخل كلمة تمثل ال spam mail 
#عملنا split() عشان  نعملها list وتحويل ال text اللى اليوزر بيدخلة ويحولها ل list
#عملنا split( بردك عشان يعرف يفحص كل حرف داخل الlist)
#وهكذا فى كل ال spam الاول والثانى والثالث والرابع
spam_email_first=input("plz enter the first spam mail: ").split()

print(spam_email_first)

spam_email_second=input("plz enter the second spam mail: ").split()

print(spam_email_second)

spam_email_third=input("plz enter the third spam mail: ").split()

print(spam_email_third)

spam_email_fourth=input("plz enter the fourth spam mail: ").split()

print(spam_email_fourth)
#بطلب من اليوزر يدخل كلمة تمثل ال ham mail 
#عملنا split() عشان  نعملها list وتحويل ال text اللى اليوزر بيدخلة ويحولها ل list
#عملنا split( بردك عشان يعرف يفحص كل حرف داخل الlist)
#وهكذا فى كل ال ham الاول والثانى والثالث والرابع
Ham_email_first=input("plz enter the first Ham mail: ").split()

print(Ham_email_first)

Ham_email_second=input("plz enter the second Ham mail: ").split()

print(Ham_email_second)

Ham_email_third=input("plz enter the third Ham mail: ").split()

print(Ham_email_third)

Ham_email_fourth=input("plz enter the fourth Ham mail: ").split()

print(Ham_email_fourth)

#لجمع ال spam mail &ham mail فى list وذالك لعمل بالظبط زى ليست داخل ليست كالاتى [[]][][]] ولل ham نفس النظام بردك..ثم طباعتهم بشكل منفرد
spam_lists=[spam_email_first,spam_email_second,spam_email_third,spam_email_fourth]

print(spam_lists)

Ham_lists=[Ham_email_first,Ham_email_second,Ham_email_third,Ham_email_fourth]

print(Ham_lists)

#لحساب الوزن (كنسبة من الإجمالى) بتاع ال spam mail
#هنحسب ثقل ميلات الspam = عدد إيميلات الspam / (عدد إيميلات الspam+ عدد إيميلات الham)
#calculating the weight of spam mail

weight_of_spam=len(spam_lists)/(len(Ham_lists)+len(spam_lists))

print(weight_of_spam)

#لحساب الوزن (كنسبة من الإجمالى) بتاع ال Ham mail
#هنحسب ثقل ميلات الham = عدد إيميلات الham / (عدد إيميلات الspam+ عدد إيميلات الham)
#calculatingthe weight of Ham mail
weight_of_Ham=len(Ham_lists)/(len(Ham_lists)+len(spam_lists))
print(weight_of_Ham)

#هنا دلوقتى هطلب من اليوزر انة يدخل ميل (اى كلمة معبرة عن الميل طبعا) عشان نحسب نسبتها كمقارنة بين ال spam وال Ham وبنعمل split عشان اعرف اقطع الكلمة وافصلها عشان اعرف اقارنها بالكلمات الاساسية اللى دخلتها لل spam&Ham
#asking the user to enter the email he wants to classify
email=input("plz enter the mail you want to classify: ").split()
print(email)
#defining variabl to record the total probability of words inside
total_spam_probability=0
#extracting each word in the email needed to be determined either its spam or Ham

for word in email:
    print(word)
#هنعد عدد الwords فى كل spamlists لو اتكرر مرة هيكتب جمبية 1 وبعدين يحط علامة + ولو اتكرر تانى هيحط 1 وبعدين يكتب + ولو تالت هيحط 1 ولو اتكرر هيكتب 1 وهكذا..وبعدين عدد المرات دى بتتسجل فى الword_spam_reapeting
#calculating the probability for the word
    word_spam_repeating=sum(x.count(word)
    for x in spam_lists)
    print(word_spam_repeating)
    
    word_Ham_repeating=sum(x.count(word)
    for x in Ham_lists)
    print(word_Ham_repeating)    
#نسبة الspam ميل( إحتمالية ان الميل يكون spam ) = (عدد مرات تكرار كلمات الspam*ثقل الميل فى الspam)/(الاجمالىْ-(عدد مرات تكرار كلمات الspam*ثقل الميل فى الspam)+(عدد مرات تكرار كلمات الham*ثقل الميل فى الham)-)
#الرقم 1 فى البسط والرقم 1 فى المقام..عشان مايدنيش error لو النتيجة كان صفر على صفر
probability_spam_for_the_word=(word_spam_repeating*weight_of_spam+1)/((word_spam_repeating*weight_of_spam)+(word_Ham_repeating*weight_of_Ham)+1.1)

print(probability_spam_for_the_word)

#calculating the new total probability for the words extracted
total_spam_probability=total_spam_probability+probability_spam_for_the_word

print(total_spam_probability)

#calculating the email spam probability

email_spam_probability=total_spam_probability/len(email)

print(email_spam_probability)