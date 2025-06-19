<div align="center">
  <p>
    <a align="center">
      <img width="550" src="https://github.com/FTDS-assignment-bay/p2-final-project-ftds-027-hck-group-001/blob/main/aerecommend.png"></a>
  </p>
</div>

## Introduction
Di era ini, smartphone telah menjadi alat penting untuk mendukung aktivitas sehari-hari. Di antara berbagai merek smartphone yang tersedia di pasar, produk Apple, yaitu iPhone, menonjol sebagai yang paling populer di seluruh dunia. Hal ini dibuktikan oleh kinerja pasar yang kuat dari seri iPhone 13 dan 14, yang memimpin peringkat penjualan smartphone global pada tahun 2023

## Problem Background
Berdasarkan dominasi global iPhone—terutama seri iPhone 13 dan 14 pada tahun 2023—kami melihat peluang besar untuk membantu brand, distributor, dan retailer dalam memahami preferensi calon user, mengidentifikasi faktor kunci yang memengaruhi keputusan pembelian, dengan merancang sistem rekomendasi. Dengan pendekatan analitik dan pembuatan model deep learning BERT, kami dapat membantu distributor dalam mempermudah calon user melalui sistem rekomendasi yang kami buat.

## Objectives
Project ini bertujuan untuk membuat sistem rekomendasi bagi calon pembeli iPhone untuk menentukan tipe iPhone series mana yang sesuai dengan kebutuhan sesuai preferensi masing-masing. Model Deep Learning yang digunakan adalah BERT dari Google. Prosesnya mencakup eksplorasi data, analisis visual, pelatihan model, evaluasi dengan metrik **f1-score**.

## Demo
### LSTM With Google BERT Preprocessing and Encoder Layer
Model bisa di train setelah mengekstrak file rar bernama best_model. Ekstrak file tersebut dan jalankan file juypyter notebook bernama best_model.ipynb, dan pastikan file model di folder yang sama dengan file notebook.

## Conclusion
- User yang membeli iPhone rata-rata senang dengan kualitas fitur kamera dan display. 
- User yang memberikan review fitur baterai beragam antara positif dan negatif.
- Model yang dibuat cukup baik dalam memprediksi pembeli yang cocok dengan iPhone 13 dan tidak buruk pada user yang diprediksi cocok dengan iPhone 14. Pada user yang diprediksi cocok dengan iPhone 15, nilai f1 score yang rendah disebabkan oleh data yang tidak seimbang, sehingga model sangat buruk dalam prediksi.

## Further Recommendations
- Memperbanyak jumlah data.
- Menggunakan model yang lebih efisien.
- Dapat merekomendasikan bukan hanya tipe tetapi dengan varian juga.

## Meet our team
* Bagus Rifky Riyanto | [LinkedIn](www.linkedin.com/in/bagusrifkyriyanto)
* Dwi Adhi Widigda Kartomihardjo | [LinkedIn](https://www.linkedin.com/in/dwi-adhi-widigda-k-641a62208/)
* Farras Annisa | [LinkedIn](https://www.linkedin.com/in/farras-annisa/)
* Iriel Aureleo | [LinkedIn](https://www.linkedin.com/in/irielaureleo/)

## URL
- Dataset URL: https://www.kaggle.com/datasets/mrmars1010/iphone-customer-reviews-nlp <br>
- Deployment URL: https://huggingface.co/spaces/DwiA2/Final_Project_Reco-ae
