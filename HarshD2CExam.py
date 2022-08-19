
import random


#def get_random_str(main_str, substr_len):
#    idx = random.randrange(0, len(main_str) -substr_len + 1)    # Randomly select an "idx" such that "idx + substr_len <= len(main_str)".
#    return main_str[idx : (idx+substr_len)]
    
#print(get_random_str("0101",2))

test_str="1001"
#res = [test_str[i: j] for i in range(len(test_str)) for j in range(i + 1, len(test_str) + 1)]
#print (str(res))
S1_SubStrings=[]
S2_SubStrings=[]
S1="1111"
for i in range (len(S1)):
	for j in range(i+1,len(S1)+1):
		#print(S1[i:j])
		S1_SubStrings.append(S1[i:j])
#print(S1_SubStrings)		
S2="1000"
for i in range (len(S2)):
	for j in range(i+1,len(S2)+1):
		#print(S2[i:j])
		S2_SubStrings.append(S2[i:j])
#print(S2_SubStrings)
final=0
for k1 in S1_SubStrings:
	for k2 in S2_SubStrings:
		if len(k1)==len(k2):
			#print(k1,k2)
			#print(len(k1)/(2*()))
			xorCount=(int(k1))^(int(k2))
			if xorCount != 0:
				result1=int(len(k1)/(2*(xorCount)))
				if final<result1:
					final=result1
print(final)
				
