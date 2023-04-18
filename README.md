# TelephoneDirectory

Bu program, kullanıcıya bir telefon rehberi uygulaması sunar ve kullanıcının rehberdeki kayıtları listeleme, kayıt arama, yeni kayıt ekleme ve kayıt silme gibi işlemleri yapmasına olanak tanır. Kısaca programın amacı, kullanıcının telefon rehberini yönetmesine yardımcı olmaktır.

Programda kullanılan ana fonksiyonlar şunlardır:

DisplayMenu(): Menüyü ekrana yazdırır ve kullanıcıya seçenekleri gösterir.
MenuLoop(): Kullanıcıdan seçim yapmasını ister ve geçerli bir seçenek girene kadar kullanıcıdan girdi almayı sürdürür.
MainLoop(): Kullanıcının seçtiği işleme göre ilgili fonksiyonları çağırarak uygulamanın ana döngüsünü oluşturur.
ListRecord(): Rehberdeki kayıtları listeler.
SearchRecord(): Rehberdeki kayıtları isim ve soyisime göre arar.
AddRecord(): Yeni bir kayıt ekler.
DeleteRecord(): Rehberden kayıt siler.
AreYouSure(): Kullanıcıya silme işlemi için onay sorar.
ReadFile(): Kayıtları dosyadan okur.
WriteFile(recordListParam : list): Kayıtları dosyaya yazar.
SearchRecordFromFile(nameparam:str, surnameparam:str): Dosyadaki kayıtları isim ve soyisime göre arar.
AddRecordToFile(nameparam:str, surnameparam:str, telnoparam:str): Dosyaya yeni bir kayıt ekler.
DeleteRecordFromFile(recordListParam : list): Dosyadan kayıt siler.
Program, kullanıcıdan alınan girdilere göre rehberdeki kayıtları yönetmekte ve kayıtları dosyada tutarak kalıcı bir veri saklama sağlamaktadır.
