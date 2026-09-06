# BÀI TẬP: PHÂN LOẠI HOA IRIS BẰNG NAIVE BAYES
# Phương pháp đánh giá: Hold-out
# Dtrain = 2/3 D
# Dtest  = 1/3 D
# Tối ưu: lựa chọn tham số var_smoothing

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# 1. ĐỌC DỮ LIỆU IRIS

df = pd.read_csv("iris.csv")

print("===== THÔNG TIN DATASET =====")

print("Số mẫu:", len(df))
print("Số thuộc tính:", len(df.columns) - 1)

print("\nTên các cột:")
print(df.columns.tolist())


# 2. TÁCH DỮ LIỆU

# 4 cột đầu tiên là các thuộc tính của hoa
X = df.iloc[:, 0:4].values

# Cột cuối cùng là tên loài hoa
y = df.iloc[:, 4].values

# 3. MÃ HÓA TÊN LOÀI HOA

encoder = LabelEncoder()

y = encoder.fit_transform(y)

print("\nCác lớp:")

for i, name in enumerate(encoder.classes_):
    print(i, ":", name)


print("\n4 thuộc tính:")

for feature in df.columns[:4]:
    print("-", feature)

# 4. CHIA DỮ LIỆU THEO HOLD-OUT
#    Train = 2/3
#    Test  = 1/3

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=1/3,
    random_state=42,
    stratify=y
)

print("\n===== CHIA DỮ LIỆU =====")

print("Tổng số mẫu:", len(X))

print("Số mẫu Training:", len(X_train))
print("Số mẫu Testing :", len(X_test))

# 5. HUẤN LUYỆN NAIVE BAYES MẶC ĐỊNH

model = GaussianNB()

model.fit(X_train, y_train)


# Dự đoán
y_pred = model.predict(X_test)


# Tính độ chính xác
accuracy = accuracy_score(y_test, y_pred)


print("\n===== NAIVE BAYES MẶC ĐỊNH =====")

print("Accuracy:", accuracy)


# 6. CONFUSION MATRIX

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")

print(cm)


# 7. CLASSIFICATION REPORT

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=encoder.classes_
    )
)

# 8. TỐI ƯU THAM SỐ var_smoothing

print("\n===== TỐI ƯU THAM SỐ =====")


params = [
    1e-12,
    1e-11,
    1e-10,
    1e-9,
    1e-8,
    1e-7,
    1e-6,
    1e-5,
    1e-4,
    1e-3
]


best_param = None
best_accuracy = 0


for value in params:

    # Tạo mô hình với tham số đang thử
    model = GaussianNB(
        var_smoothing=value
    )

    # Huấn luyện
    model.fit(X_train, y_train)

    # Dự đoán
    y_pred = model.predict(X_test)

    # Tính Accuracy
    accuracy = accuracy_score(
        y_test,
        y_pred
    )

    print(
        f"var_smoothing = {value:<10} "
        f"Accuracy = {accuracy:.4f}"
    )


    # Lưu tham số tốt nhất
    if accuracy > best_accuracy:

        best_accuracy = accuracy
        best_param = value


# 9. HIỂN THỊ THAM SỐ TỐI ƯU

print("\n===== KẾT QUẢ TỐI ƯU =====")

print("Tham số tốt nhất:", best_param)

print("Accuracy tốt nhất:", best_accuracy)


# 10. HUẤN LUYỆN LẠI VỚI THAM SỐ TỐT NHẤT

best_model = GaussianNB(
    var_smoothing=best_param
)

best_model.fit(
    X_train,
    y_train
)

y_best_pred = best_model.predict(
    X_test
)

# 11. ĐÁNH GIÁ MÔ HÌNH SAU KHI TỐI ƯU

print("\n===== MÔ HÌNH SAU KHI TỐI ƯU =====")


final_accuracy = accuracy_score(
    y_test,
    y_best_pred
)

print("Accuracy:", final_accuracy)


print("\nConfusion Matrix:")

print(
    confusion_matrix(
        y_test,
        y_best_pred
    )
)


print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_best_pred,
        target_names=encoder.classes_
    )
)

# 12. THỬ DỰ ĐOÁN MỘT BÔNG HOA MỚI

print("\n===== DỰ ĐOÁN MẪU MỚI =====")


# [Sepal Length, Sepal Width, Petal Length, Petal Width]

flower = [
    [5.1, 3.5, 1.4, 0.2]
]


# Dự đoán
prediction = best_model.predict(
    flower
)


print("Mẫu hoa:", flower)

print(
    "Dự đoán:",
    encoder.inverse_transform(prediction)[0]
)

# 13. XÁC SUẤT DỰ ĐOÁN

probability = best_model.predict_proba(
    flower
)


print("\nXác suất dự đoán:")


for name, prob in zip(
    encoder.classes_,
    probability[0]
):

    print(
        f"{name}: {prob:.4f}"
    )
