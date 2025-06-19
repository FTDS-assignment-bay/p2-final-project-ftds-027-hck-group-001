<div align="center">
  <p>
    <a align="center">
      <img width="550" src="https://github.com/FTDS-assignment-bay/p2-final-project-ftds-hck-026/blob/dev-tina/LOGO%20AISEE%20YOU.png"></a>
  </p>
</div>

## Introduction
Di era ini, smartphone telah menjadi alat penting untuk mendukung aktivitas sehari-hari. Di antara berbagai merek smartphone yang tersedia di pasar, produk Apple, yaitu iPhone, menonjol sebagai yang paling populer di seluruh dunia. Hal ini dibuktikan oleh kinerja pasar yang kuat dari seri iPhone 13 dan 14, yang memimpin peringkat penjualan smartphone global pada tahun 2023

## Problem Background
Berdasarkan dominasi global iPhone—terutama seri iPhone 13 dan 14 pada tahun 2023—kami melihat peluang besar untuk membantu brand, distributor, dan retailer dalam memahami preferensi calon user, mengidentifikasi faktor kunci yang memengaruhi keputusan pembelian, dengan merancang sistem rekomendasi. Dengan pendekatan analitik dan pembuatan model deep learning BERT, kami dapat membantu distributor dalam mempermudah calon user melalui sistem rekomendasi yang kami buat.

## Objectives
Project ini bertujuan untuk membuat sistem rekomendasi bagi calon pembeli iPhone untuk menentukan tipe iPhone series mana yang sesuai dengan kebutuhan sesuai preferensi masing-masing. Model Deep Learning yang digunakan adalah BERT dari Google. Prosesnya mencakup eksplorasi data, analisis visual, pelatihan model, evaluasi dengan metrik **f1-score**.

## Demo
### YOLOv8 Model
1. To get started, visit the provided [link](https://deployment-5rznu7uyrh43hms2ce7vh5.streamlit.app/) to access the application.
2. Once you have logged into the application, you will see several page options to explore. To find out when dangerous objects are most likely to be detected, please select the 'X-ray Detection Prediction' page.

### Faster R-CNN w/ResNet50
Download the trained model from this [Google Drive link](https://drive.google.com/file/d/1T4EIeSrLjLdQ3Bk2YBNywTcSX5QoTBlL/view?usp=sharing), extract the content and put it in the root folder of the repository.
Alternatively, you can train and build your own model. Follow the guide at [TensorFlow README.md](TensorFlow%20README.md) to train and run your own model.

## Conclusion
The model is able to detect dangerous objects from X-ray images effectively.
Based on evaluations using Ultralytics, the model achieved a performance of over 80% mAP@0.5.
This result provides a strong foundation for further development, both in improving accuracy and expanding the scope of hazardous object detection.

## Further Recommendations
1. **Increasing the Number of Data Samples:** 
Adding more data helps the model learn from a wider variety of examples, which improves its ability to detect dangerous objects in real-world scenarios. A larger dataset reduces the risk of overfitting and enhances generalization.

2. **Data Augmentation:** Data augmentation involves applying transformations—such as rotation, scaling, flipping, or adding noise—to existing images. This technique increases the diversity of the training data without the need to collect new samples, making the model more robust to different angles, sizes, and distortions.

3. **Fine-Tuning:** Fine-tuning is the process of taking a pre-trained model and adapting it to a specific dataset. This allows the model to leverage previously learned features while focusing on the unique characteristics of X-ray images, leading to higher detection accuracy.

4. **Trying Different Model Architectures:** Exploring alternative model architectures (e.g., YOLOv8, EfficientDet, or Faster R-CNN) can help identify one that better balances speed, accuracy, and resource efficiency for X-ray object detection tasks. Each architecture has strengths that may suit specific use cases.

## Meet our team
* Zaky Rizky Akbar | [LinkedIn](https://www.linkedin.com/in/zaky-rizky-akbar-894332171/) | [Github](https://github.com/zakyrizky05) 
* Maulana Yusuf Taufiqurrahman| [LinkedIn](https://www.linkedin.com/in/maulana-yusuf-taufiqurrahman-5281662a2) | [Github](https://github.com/Maulana-Yusuf-T)
* Angga Fadhlurrahman Prianto | [LinkedIn](www.linkedin.com/in/angga-fadhlurrahman-prianto-29501b194) | [Github](https://github.com/angga7353)
* Muhammad Irfan Hilmi| [LinkedIn](https://www.linkedin.com/in/muhammad-irfan-hilmi-90a282241/) | [Github]( https://github.com/Hennoshin)
* Suartina Sitanggang | [LinkedIn](https://www.linkedin.com/in/suartinasitanggang/) | [Github](https://github.com/tinaSTG)


## References
https://github.com/ultralytics/yolov5/<br>
https://www.kaggle.com/datasets/orvile/x-ray-baggage-anomaly-detection/data <br>
https://www.tensorflow.org/api_docs/python/tf#tensorflow