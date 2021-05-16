import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from skimage.feature import hog
from skimage.io import imread
from skimage.transform import resize

def main():
    working_directory = os.path.dirname(os.getcwd()) + os.path.sep + 'imagesToProcess' + os.sep
    
    available_categories = os.listdir(working_directory)
    number_of_categories = 6
    categories_to_work = []
    working_data = []
    
    while len(categories_to_work) != number_of_categories:
        random_category = available_categories[np.random.randint(0,len(available_categories))]
        if random_category not in categories_to_work:
            categories_to_work.append(random_category)
    categories_to_work.sort()
    
    print("Categories that are available in this execution:")
    for i in range(0, len(categories_to_work)):
        print(categories_to_work[i])
    
    for category in categories_to_work:
        working_path = os.path.join(working_directory, category)
        label = categories_to_work.index(category)
        
        for image in os.listdir(working_path):
            image_path = os.path.join(working_path, image)
            image_to_get = imread(image_path, as_gray=True)
            
            try:
                image_to_get = resize(image_to_get, (150, 150))
                image_to_get_hog, image_to_get_hog_img = hog(
        image_to_get, pixels_per_cell=(14,14), 
        cells_per_block=(2, 2), 
        orientations=9, 
        visualize=True, 
        block_norm='L2-Hys')
                image_to_add = np.array(image_to_get).flatten()
                working_data.append([image_to_get_hog, label, image_to_add])
            except:
                pass
            
            
    features = []
    labels = []
    images = []
    
    for feature, label, image in working_data:
        features.append(feature)
        labels.append(label)
        images.append(image)
        
    x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, shuffle=True, random_state=42)
    model_1 = SVC(C=1.0,kernel='linear', gamma='auto')
    
    model_1.fit(x_train,y_train)
    
    prediction_1_HOG = model_1.predict(x_test)
    
    accuracy_1_HOG = model_1.score(x_test,y_test)
    
    print()
    print("Accuracies by HOGs: ")
    print()
    print("Accuracy by 'linear': " + str(accuracy_1_HOG))
    
    x_test_number = []
    x_test_image = []
    
    for prediction in range(len(x_test)):
        if (prediction_1_HOG[prediction] not in x_test_number) and (prediction_1_HOG[prediction] == y_test[prediction]):
            x_test_number.append(prediction_1_HOG[prediction])
            x_test_image.append(x_test[prediction])
    
    feature_number_1 = []
    
    fig, ax = plt.subplots(1,len(x_test_number))
    fig.tight_layout(pad=2.0)
    fig.set_size_inches(10,2)
    
    [a.tick_params(bottom=False, left=False, labelbottom=False, labelleft=False) 
        for a in ax]
    
    for test in range(len(x_test_number)):
        for feature in range(len(features)):
            if list(x_test_image[test]) == list(features[feature]) and (feature not in feature_number_1):
                feature_number_1.append(feature)
            
    for feature in range(len(feature_number_1)):
        ax[feature].imshow(images[feature_number_1[feature]].reshape(150,150), cmap='gray')
        ax[feature].set_title(str(categories_to_work[x_test_number[feature]]))

    path_to_save = os.getcwd() + os.path.sep + 'random_execution_results.png'
    plt.savefig(path_to_save)    
    plt.show()

if __name__ == "__main__":
    main()