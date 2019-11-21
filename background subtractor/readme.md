# Counting Car With Background subtractor
Bu projede bir şeritten geçen araç sayısını background subractor kullanarak saymayı hedeflenmiştir.
Çalışma mantıgı ise ilk videodan veya kameradan bir frame alıyor ve bir sonraki aşamada bu frame den yeni frami çıkarıyor.
<img src='https://github.com/yunusaltuntas/opencv-project/blob/master/background%20subtractor/working_method.PNG' width='500'>

Çıktımızı bir tresholdan geçirerek binary görüntü formatına dönüştürüyoruz.
Findcontours metodu ile nesnemizin konumunu buluyoruz
Ardından belirlenen bu iki çizgi arasından geçen nesne oldugunda counter ı arttırarak araç sayma işlemini bu örnekte gerçekleştirmiş bulundum.
