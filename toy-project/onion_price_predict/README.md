# 파를 먹고 싶어요! 알려주세요 MLP
> toy project

- 프로젝트 시작 이유?
- 파절이는 삽겹살의 소울 프렌드인데....
- But 미쳐가는 파가격 때문에 살까 말까 고민을 하다가 개발하게 되었습니다.

> 가정
- **오늘의 파 가격**은 어제 최고,최저,평균 온도, 강수량, 파가격으로 예측 가능할것이다.

> Project Flow

![Screenshot from 2021-05-12 15-43-04](https://user-images.githubusercontent.com/72845895/117930295-ca63a300-b338-11eb-9b1d-42e0a79d8c2c.png)


> 사용 모델 
- tensorflow version 2.6.0 night version
- MLP(3 layers linear regression)  
- 과적합을 피하기 위해 dropout 사용 


![Screenshot from 2021-05-12 16-07-55](https://user-images.githubusercontent.com/72845895/117933358-73f86380-b33c-11eb-90e5-5643ed3d0beb.png)


> Parameter
- learning-rate = 000005
- epoch = 10000
- batchsize = 8
- callback = earlystop

> 결과 
- model 성능 True vs Prediction 
![Screenshot from 2021-05-12 16-21-09](https://user-images.githubusercontent.com/72845895/117934895-19600700-b33e-11eb-9a6b-1dc98d1b24f0.png)

---

- console 창 결과 
    - 최근 30일 평균 파 가격 보다 예측된 파 가격이 싸다면 사세요!!
    - 최근 30일 평균 파 가격 보다 예측된 파 가격이 비싸면 참으시에요!! 출력되게 구성
![Screenshot from 2021-05-12 19-52-43](https://user-images.githubusercontent.com/72845895/117963710-ad8c9700-b35b-11eb-9d94-030fdb7fa89d.png)

> FIN 파절이 삼겹살 먹으로 가야지!! 

![Screenshot from 2021-05-12 18-55-59](https://user-images.githubusercontent.com/72845895/117956145-baa58800-b353-11eb-883d-01be1b36ca5d.png)


> 느낌점
- 데이터 수집이 조금 더 길었으면 좋았겠다라는 생각을 했습니다.
- 추가 컬럼이 조금만 더 있으면 좋을것 같습니다.
