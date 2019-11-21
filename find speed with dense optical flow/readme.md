# Find Speed With Dense Optical Flow
Bu projede optical flow yöntemi kullanarak araç hız tespit projesi yapılmıştır.

<img src='https://github.com/yunusaltuntas/opencv-project/blob/master/find%20speed%20with%20dense%20optical%20flow/working-method.PNG' width='400'>
Görüntüden belli noktalardan keypoinler alınır ve bu keypointle bir sonraki frame de hangi noktada bulundugu tespit edebiliriz.
Keypoinler görüntüde ne kadar hızla hareket ettiklerini X=v*t den bulabiliriz. .Hızlarını bulmak için aldıkları yolu geçirdikleri süreye bölerek hızını buluyoruz.
Bu örnekte iki adet çizgi belirlenmiştir bu çigileri geçiş zamanları kaydedilir. İki çizgi arasındaki mesafe keypointimizin bu iki çizgi arasında bulundugu süreye bölünerek hızını elde ettik.
