from abc import ABC, abstractmethod

class Image(ABC):
    @abstractmethod
    def load_image(self, filename):
        pass
    
    @abstractmethod
    def save_image(self, filename):
        pass

class Bitmap(Image):
    def load_image(self, filename):
        print(f"Loading bitmap image from {filename}")
        
    def save_image(self, filename):
        print(f"Saving bitmap image to {filename}")

class Jpeg(Image):
    def load_image(self, filename):
        print(f"Loading JPEG image from {filename}")
        
    def save_image(self, filename):
        print(f"Saving JPEG image to {filename}")


bitmap_image = Bitmap()
bitmap_image.load_image("kku.bmp")
bitmap_image.save_image("kku.bmp")

jpeg_image = Jpeg()
jpeg_image.load_image("en.jpg")
jpeg_image.save_image("en.jpg")
