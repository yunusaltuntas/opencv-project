# Counting Car With Background Subtractor
Bu projede şeritten geçen araçlarını sayılması hedeflenmiştir.Görüntü üzerine çekilen bir çizgiden araçlar geçtigi zaman counter bir artırılarak bu işlem gerçekleştirilmiştir.
<img src='https://github.com/yunusaltuntas/opencv-project/blob/master/counting%20car%20with%20background%20subtractor/working_method.PNG' with='300'>

Kamera veya video vasıtasıyla alınan görüntülerden ard arda alınan iki frame birbirinden çıkartılır.Bu çıkartılan frameler belli bir treshold dan geçirilerek binary formatına dönüştürülür
Bu işlemden sonra nesnemiz beyaz olarak, yani bulundugu pixeller 1 olarak ifade edilir.Findcontour metodu ile genişliği ve konumu gibi verilere ulaşırız.Bu verileri kullanarak nesnemizin belirledigimiz çizginin diger tarafına geçtigi durumda counter u bir arttırıyoruz ve ekrana yazdırıyoruz.
