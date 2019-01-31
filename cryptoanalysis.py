import array
import matplotlib.pyplot as plt
def char_frequency(file1):
	dict = {}
	prob=[0]*100000
	str2=[]*100000
	word2=[]
	file2=open("textfile","r")
	str1=file2.read()
	names=[]
	values=[]
	length=[0]*26
        table=[8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.996,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074]
	total=len(str1)
	min=1000
	str1=str1.lower()



	#encryption
	for i in range(0,total):
		if(str1[i]=='z'):
			word2.append((chr(ord(str1[i])-25)))
		else:
			word2.append((chr(ord(str1[i])+1)))
	strr=''.join(word2)
	#print(strr)

	#freq

	for n in strr:
		keys = dict.keys()
		if n in keys:
			dict[n] += 1
		else:
			dict[n] = 1
	print(keys)




	#to delete some unwanted keys from dict
	#for i in keys:
	#	if(keys==
	#del dict[""]
	#print(keys)


	
	no_of_letters_encr=0
	for n in strr:
	    prob[no_of_letters_encr]=((dict[n]/float(total))*100)
	    no_of_letters_encr=no_of_letters_encr+1
	
	for i in range(0,total):
		min=1000
		for j in range(0,26):
		    if(min>abs(float(prob[i]-table[j]))):
				min=abs(float(prob[i]-table[j]))
				k=j
	        str2.append(chr(ord('a')+k))
		
	print(''.join(str2))
	#accuracy
	count_correct=0
	j=0
	for i in str1:
		
		
		if(str2[j]==str1[j]):
			count_correct=count_correct+1
		j=j+1
	acc=(count_correct/float(j))*100
	print("accuracy:",acc)
	print("correct lettercount:",count_correct)
	print("no. of letters in encryption given:",no_of_letters_encr)


	#for matplotlib
	for i in keys:
		if(i.isalpha()):
			names.append(i)
			values.append((dict[i]/float(total))*100)


	#for first param
	for i in range(0,26):
		length[i]=i
	
	print(names)
	print(values)
	print(len(names))
	print(len(values))
	#names=list(dict.keys())
	#values=list(dict.values())
	#range(len(dict))
	plt.bar(length,values,tick_label=names)
	#plt.bar([1,2,3],[10,20,30],tick_label=['apple','mango','pineapple'])
	plt.savefig('bar.png')
	plt.show()
		




def main():
	#char_frequency("icameintothisworldonoctandguesswhatiwasdamnprettyasachildmymomtellsethisiknoweveryparentliketheirkidbuttrustmeiwasdamncuteihaveseenthepicturessomylifewhatcanisayaboutmylifeitsprettyhardtowriteaboutitbecauseilivedmylifeandwhateveryoulivedcannotbeexpressedinwordsbutstilliwilltrytowritebecauseiwanttodosomethingwhichwillstayevenifidieandthisisthebestthingicandoforitherewegoicameintothisworldon11oct1998andguesswhatiwasdamnprettyasachildmymomtellsmethisiknoweveryparentliketheirkidsbuttrustmeiwasdamncuteihaveseenthepicturessoiwasborninabusinessfamilybutactuallybeforemybornmyfatherusedtoworkasacivilengineerinbhopalbutjustbecausemygrandfatherandtwootherunclewereunabletocarryonthefamilybusinessmyfatherwascalledtoleavehisjobandunfortunatelyhehadtocometofirozabadadistrictinuttarpradeshiwasborninfirozabadandyouknowwhatineverregrettedlivingtherebecauseitsverydifferenttoliveinsmalltownandthebestpartisigottolivewithmygrandparentswhichisaspecialthingnoteveryonegetstoenjoythatandasakidyougettolearnalotfromthemsowhenibecameaoneyearoldkidmymomstartedtoteachhindimediumstudentsbtwmymomisamathsteacheranditsnotabigdealbutiamreallyproudofmymomdonttellherbutsheissmartxdohiforgottotellyouguysinmyhomememyparentsgrandparentsmyannoyingelderbrotherginnidiandgullubhaiyausedtolivesomyauntandunclepassedawayinanaccidentsotheirkidsusedlivewithusandiusedtoadmireginnidishewassoprettyandcalmthiswasmyfamilybackgroundnowiwilltalkaboutmyselfiwasahappykidineverusedtocrythatswhatmyfamilytoldmebutnowidocrysohereisoneevidenceofmenotcryingmymomtookmetoadoctortogetvaccinationdoneandtherehewasputtinginjectionandistartedlaughingxddoctoraskedmymomifiwasabnormalitssoundsfunnynowbutimaginewhatmymomthoughtaboutitxditurned2andahalfwhenistartedgoingtoschoolandithinkiwasthefirstkidevertogotoschoolhappilymymom"says"ilookedverycuteinthatuniform:)likethisigrewupandstartedrememberingthingsandirememberishatinmypantswhilestandinginpunishmentinmyfirstgradeandtillmyfirststandardihadtheworstfriendstheyusedtomakemelearnsomebadshitirememberonewasmonuanddontgowiththenameshewasagirliwasnotthatgoodinacademicsandasitoldyoumymomwasateacherandsheexpectedmetobegoodbutiwasntbutsomehowshemanagedmetobeanaveragestudentsheusedtomakelearnmathsproblemstobeparticularsheusedtoteachmeifyouseeeachinquestionthenjustdividethebignotosmalloneandwriteasananswerasitoldihadbadfriendssoheresonefunnyincidentweusedtohaveparentsmeetinginschoolaftereveryunittestsoigot19marksoutof20inmathsandmymomwashappyandthenmyfriendcomestomeandsheasksmehowmuchdidigetinmathsitoldheronemarkilostandshethoughtigotonlyoneandshestartedlaughingandgivingmehighfivebecauseshegot2andmymomwassodisappointedsolaterinmysecondgradeithoughtofmakingnewfriendsandforthegoodmyoldfriendsleftmyschoolsoitwaseasytomakenewfriendswithouthavingaguiltsotherewasagirlinvishewassmarttooandherparentswerealsodoctorsoneverthoughtiwillbegoodfriendswiththembecausemanaviwasnotopenupinmyschooltherewerebencheswhichcanaccomodate3peoplesoitwaslikeadreamforeveryonetositnexttothesetwogirlsandguesswhatidintsitthemxdtherewasagirlcalledjagratishewasprettyandshewasanaveragestudentsheusedtositwiththemthenigot")
	char_frequency("textfile")
if __name__ == "__main__":
	main()
