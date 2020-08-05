# 사용자로부터 국어, 수학, 영어 점수를 입력받아 합계, 평균을 구하고 등급 매기기
kor,mat,eng=input("국어, 수학, 영어 점수를 입력하시오").split()
total=int(kor)+int(mat)+int(eng)
ave=total/3
print(total, ave)
if ave >= 90:
    print('총점 :',total,', 평균 :',ave,', 당신의 학점은 A')
elif ave >= 80:
    print('총점 :',total,', 평균 :',ave,', 당신의 학점은 B')
elif ave >= 70:
    print('총점 :',total,', 평균 :',ave,', 당신의 학점은 C')
elif ave >= 60:
    print('총점 :',total,', 평균 :',ave,', 당신의 학점은 D')
else:
    print('당신의 학점은')

