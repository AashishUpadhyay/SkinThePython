# Reservoir Sampling Explained

Given an array arr of length N, select k elements randomly such that each element has an equal probability of selection

example arr = [11,2,13,234,225,36,17]
k = 3

lets create a reservoir array r_arr of first k elements [11,2,13]

## For elements having index >= 3

### P(1): Probability of an element at index i; i.e.(3,4,5,6) getting selected for replacing an existing element in r_arr

* For i = 3, the probability of arr[3] i.e. 234 getting selected and replacing an element in r_arr = 3/4
* For i = 4, the probability of arr[4] i.e. 225 getting selected and replacing an element in r_arr = 3/5
* For i = 5, the probability of arr[5] i.e. 36 getting selected and replacing an element in r_arr = 3/6
* For i = 6, the probability of arr[6] i.e. 17 getting selected and replacing an element in r_arr = 3/7

### P(2): Probability of not getting replaced by items at index > i
 
* For i = 3:
 The probability of 234 not getting replaced:
    (probability of arr[4] not replacing 234 = probability of arr[4] not getting selected i.e. (1-3/5) + probability of arr[4] getting selected but replacing other elements than 234 i.e. (3/5*2/3)) * 
    (probability of arr[5] not replacing 234 = probability of arr[5] not getting selected i.e. (1-3/6) + probability of arr[5] getting selected but replacing other elements than 234 i.e. (3/6*2/3))
    (probability of arr[6] not replacing 234 = probability of arr[6] not getting selected i.e. (1-3/7) + probability of arr[6] getting selected but replacing other elements than 234 i.e. (3/7*2/3))
* For i = 4:
 The probability of 225 not getting replaced:
    (probability of arr[5] not replacing 225 = probability of arr[5] not getting selected i.e. (1-3/6) + probability of arr[5] getting selected but replacing other elements than 225 i.e. (3/6 * 2/3)) * 
    (probability of arr[6] not replacing 225 = probability of arr[6] not getting selected i.e. (1-3/7) + probability of arr[6] getting selected but replacing other elements than 225 i.e. (3/7 * 2/3))  
* For i = 5:
 The probability of 36 not getting replaced:
    (probability of arr[6] not replacing 36 = probability of arr[6] not getting selected i.e. (1-3/7) + probability of arr[6] getting selected but replacing other elements than 36 i.e. (3/7*2/3))  
* For i = 6:
 Since thats the ends of the array there is no replacement to occur so 0 probability

### Total probability for an index i P(3) = P(1) * P(2)

* For i = 3:
 Total probability:
  3/4 * ((1-3/5) + (3/5*2/3)) * ((1-3/6) + (3/6*2/3)) * ((1-3/7) + (3/7*2/3)) = 3/4 * (2/5 + 2*5) * (3/6 + 2/6) * (4/7 + 2/7) = 3/4 * 4/5 * 5/6 * 6/7 = 3/7 i.e. k/N
* For i = 4:
 Total probability:
  3/5 * ((1-3/6) + (3/6*2/3)) * ((1-3/7) + (3/7*2/3)) = 3/5 * (3/6 + 2/6) * (4/7 + 2/7) = 3/5 * 5/6 * 6/7 = 3/7 i.e. k/N
* For i = 5:
 Total probability:
  3/6 * ((1-3/7) + (3/7*2/3)) = 3/6 * (4/7 + 2/7) = 3/6 * 6/7 = 3/7 i.e. k/N
* For i = 6:
 Total probability:
  3/7 i.e. k/N

## For elements having index < 3 the total probability is the probability of nor getting replaced by elements at index >=3

* For i = 0:
 The probability of 11 not getting replaced:
    (probability of arr[3] not replacing 11 = probability of arr[3] not getting selected i.e. (1-3/4) + probability of arr[4] getting selected but replacing other elements than 11 i.e. (3/4*2/3)) *
    (probability of arr[4] not replacing 11 = probability of arr[4] not getting selected i.e. (1-3/5) + probability of arr[4] getting selected but replacing other elements than 11 i.e. (3/5*2/3)) * 
    (probability of arr[5] not replacing 11 = probability of arr[5] not getting selected i.e. (1-3/6) + probability of arr[5] getting selected but replacing other elements than 11 i.e. (3/6*2/3))
    (probability of arr[6] not replacing 11 = probability of arr[6] not getting selected i.e. (1-3/7) + probability of arr[6] getting selected but replacing other elements than 11 i.e. (3/7*2/3))
* For i = 1:
 The probability of 2 not getting replaced:
    (probability of arr[3] not replacing 2 = probability of arr[3] not getting selected i.e. (1-3/4) + probability of arr[4] getting selected but replacing other elements than 2 i.e. (3/4*2/3)) *
    (probability of arr[4] not replacing 2 = probability of arr[4] not getting selected i.e. (1-3/5) + probability of arr[4] getting selected but replacing other elements than 2 i.e. (3/5*2/3)) * 
    (probability of arr[5] not replacing 2 = probability of arr[5] not getting selected i.e. (1-3/6) + probability of arr[5] getting selected but replacing other elements than 2 i.e. (3/6*2/3))
    (probability of arr[6] not replacing 2 = probability of arr[6] not getting selected i.e. (1-3/7) + probability of arr[6] getting selected but replacing other elements than 2 i.e. (3/7*2/3))
* For i = 2:
 The probability of 13 not getting replaced:
    (probability of arr[3] not replacing 13 = probability of arr[3] not getting selected i.e. (1-3/4) + probability of arr[4] getting selected but replacing other elements than 13 i.e. (3/4*2/3)) *
    (probability of arr[4] not replacing 13 = probability of arr[4] not getting selected i.e. (1-3/5) + probability of arr[4] getting selected but replacing other elements than 13 i.e. (3/5*2/3)) * 
    (probability of arr[5] not replacing 13 = probability of arr[5] not getting selected i.e. (1-3/6) + probability of arr[5] getting selected but replacing other elements than 13 i.e. (3/6*2/3))
    (probability of arr[6] not replacing 13 = probability of arr[6] not getting selected i.e. (1-3/7) + probability of arr[6] getting selected but replacing other elements than 13 i.e. (3/7*2/3))


### Total probability for an index i < 3

* i = 0:
   ((1-3/4) + (3/4*2/3)) * ((1-3/5) + (3/5*2/3)) * ((1-3/6) + (3/6*2/3)) * ((1-3/7) + (3/7*2/3)) = (1/4 + 2/4) * (2/5 + 2/5) * (3/6 + 2/6) * (4/7 + 2/7) = 3/4 * 4/5 * 5/6 * 6/7 = 3/7 i.e. k/N
* i = 1:
   ((1-3/4) + (3/4*2/3)) * ((1-3/5) + (3/5*2/3)) * ((1-3/6) + (3/6*2/3)) * ((1-3/7) + (3/7*2/3)) = (1/4 + 2/4) * (2/5 + 2/5) * (3/6 + 2/6) * (4/7 + 2/7) = 3/4 * 4/5 * 5/6 * 6/7 = 3/7 i.e. k/N
* i = 2:
   ((1-3/4) + (3/4*2/3)) * ((1-3/5) + (3/5*2/3)) * ((1-3/6) + (3/6*2/3)) * ((1-3/7) + (3/7*2/3)) = (1/4 + 2/4) * (2/5 + 2/5) * (3/6 + 2/6) * (4/7 + 2/7) = 3/4 * 4/5 * 5/6 * 6/7 = 3/7 i.e. k/N
