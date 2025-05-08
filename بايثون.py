import os

images_dir = "صور"
image_files = [f for f in os.listdir(images_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))]

for img in image_files:
    img_path = f"{images_dir}/{img}"
    print(f'''
      <div class="card">
        <img src="{img_path}" alt="{img}">
        <h3>{img}</h3>
        <div class="buttons">
          <a href="{img_path}" download>تحميل</a>
          <button onclick="previewImage('{img_path}')">معاينة</button>
        </div>
      </div>
    ''')