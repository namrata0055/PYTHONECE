class Arrays:
  def array_types():
    arr_1=[1,2,3,4,5,"test",23.36,False,23+4j]
    arr_2=(1,2,3)
    arr_3={"namrata",123,569}
    arr_4={
        "name":"google",
        "age":"1000",
        "test1":"test2",
    }
    print(type(arr_1))
    print(type(arr_2))
    print(type(arr_3))
    print(type(arr_4))
Arrays.array_types()