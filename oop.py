class Smartphone:
    """Represents a basic smartphone."""

    def __init__(self, brand, model, imei, display_size, battery_capacity):
        """
        Initializes a Smartphone object.

        Args:
            brand (str): The brand of the smartphone (e.g., Samsung, Apple).
            model (str): The model name of the smartphone (e.g., Galaxy S23, iPhone 15).
            imei (str): The unique International Mobile Equipment Identity.
            display_size (float): The size of the display in inches.
            battery_capacity (int): The battery capacity in mAh.
        """
        self.brand = brand
        self.model = model
        self.imei = imei
        self.display_size = display_size
        self.battery_capacity = battery_capacity
        self._is_on = False  # Encapsulated attribute: starts off
        self._battery_level = battery_capacity  # Encapsulated attribute: starts full

    def power_on(self):
        """Turns the smartphone on."""
        if not self._is_on:
            self._is_on = True
            print(f"{self.brand} {self.model} is powering on.")
        else:
            print(f"{self.brand} {self.model} is already on.")

    def power_off(self):
        """Turns the smartphone off."""
        if self._is_on:
            self._is_on = False
            print(f"{self.brand} {self.model} is powering off.")
        else:
            print(f"{self.brand} {self.model} is already off.")

    def call(self, number):
        """Simulates making a call."""
        if self._is_on and self._battery_level > 5:
            print(f"{self.brand} {self.model} is calling {number}...")
            self._battery_level -= 5  # Simulate battery drain
        elif not self._is_on:
            print(f"Cannot make a call. {self.brand} {self.model} is off.")
        else:
            print(f"Cannot make a call. Battery level is too low.")

    def receive_call(self, number):
        """Simulates receiving a call."""
        if self._is_on:
            print(f"{self.brand} {self.model} is receiving a call from {number}.")
        else:
            print(f"{self.brand} {self.model} is off. Cannot receive call.")

    def display_battery(self):
        """Displays the current battery level."""
        print(f"{self.brand} {self.model} battery level: {self._battery_level} mAh")

    def __str__(self):
        """Returns a string representation of the smartphone."""
        return f"{self.brand} {self.model} (IMEI: {self.imei}, Display: {self.display_size}\", Battery: {self.battery_capacity} mAh)"


# Inheritance Layer for Specialized Smartphones
class GamingSmartphone(Smartphone):
    """Represents a smartphone designed for gaming, inheriting from Smartphone."""

    def __init__(self, brand, model, imei, display_size, battery_capacity, dedicated_gpu, cooling_system):
        """
        Initializes a GamingSmartphone object.

        Args:
            brand (str): The brand of the gaming smartphone.
            model (str): The model name of the gaming smartphone.
            imei (str): The unique IMEI.
            display_size (float): The size of the display.
            battery_capacity (int): The battery capacity.
            dedicated_gpu (str): The name of the dedicated graphics processing unit.
            cooling_system (str): The type of cooling system implemented.
        """
        super().__init__(brand, model, imei, display_size, battery_capacity)
        self.dedicated_gpu = dedicated_gpu
        self.cooling_system = cooling_system
        self._performance_mode = "normal"  # Encapsulated attribute

    def enable_performance_mode(self):
        """Enables high-performance gaming mode."""
        if self._is_on:
            self._performance_mode = "high"
            print(f"{self.brand} {self.model}: Performance mode enabled for optimal gaming.")
            self._battery_level -= 10  # Higher battery drain in performance mode
        else:
            print(f"Cannot enable performance mode. {self.brand} {self.model} is off.")

    def disable_performance_mode(self):
        """Disables high-performance gaming mode."""
        self._performance_mode = "normal"
        print(f"{self.brand} {self.model}: Performance mode disabled.")

    def play_game(self, game_title):
        """Simulates playing a game."""
        if self._is_on and self._battery_level > 15:
            print(f"{self.brand} {self.model} is playing {game_title} in {self._performance_mode} mode.")
            self._battery_level -= 15  # Simulate higher battery drain during gaming
        elif not self._is_on:
            print(f"Cannot play game. {self.brand} {self.model} is off.")
        else:
            print(f"Battery too low to play {game_title}.")

    def __str__(self):
        return f"{super().__str__()} (Gaming Edition, GPU: {self.dedicated_gpu}, Cooling: {self.cooling_system})"


class CameraSmartphone(Smartphone):
    """Represents a smartphone with advanced camera features, inheriting from Smartphone."""

    def __init__(self, brand, model, imei, display_size, battery_capacity, main_camera_mp, front_camera_mp):
        """
        Initializes a CameraSmartphone object.

        Args:
            brand (str): The brand of the camera smartphone.
            model (str): The model name.
            imei (str): The unique IMEI.
            display_size (float): The display size.
            battery_capacity (int): The battery capacity.
            main_camera_mp (int): Megapixels of the main rear camera.
            front_camera_mp (int): Megapixels of the front-facing camera.
        """
        super().__init__(brand, model, imei, display_size, battery_capacity)
        self.main_camera_mp = main_camera_mp
        self.front_camera_mp = front_camera_mp

    def take_photo(self):
        """Simulates taking a photo."""
        if self._is_on and self._battery_level > 2:
            print(f"{self.brand} {self.model} took a {self.main_camera_mp}MP photo.")
            self._battery_level -= 2
        elif not self._is_on:
            print(f"Cannot take photo. {self.brand} {self.model} is off.")
        else:
            print("Battery too low to take a photo.")

    def record_video(self, duration_seconds):
        """Simulates recording a video."""
        battery_drain = duration_seconds // 10  # Approximate battery drain
        if self._is_on and self._battery_level > battery_drain:
            print(f"{self.brand} {self.model} is recording a video for {duration_seconds} seconds.")
            self._battery_level -= battery_drain
        elif not self._is_on:
            print(f"Cannot record video. {self.brand} {self.model} is off.")
        else:
            print("Battery too low to record video for that duration.")

    def __str__(self):
        return f"{super().__str__()} (Camera Focused, Main Cam: {self.main_camera_mp}MP, Front Cam: {self.front_camera_mp}MP)"


# Creating instances of the classes
phone1 = Smartphone("Samsung", "Galaxy A54", "123456789012345", 6.4, 5000)
phone2 = GamingSmartphone("ASUS", "ROG Phone 7", "987654321098765", 6.78, 6000, "Adreno 740", "GameCool 7")
phone3 = CameraSmartphone("Google", "Pixel 8 Pro", "543210987654321", 6.7, 5050, 50, 10.5)

# Interacting with the objects
print(phone1)
phone1.power_on()
phone1.call("07XXXXXXXXX")
phone1.display_battery()
phone1.power_off()
print("-" * 20)

print(phone2)
phone2.power_on()
phone2.enable_performance_mode()
phone2.play_game("Asphalt 9")
phone2.display_battery()
phone2.power_off()
print("-" * 20)

print(phone3)
phone3.power_on()
phone3.take_photo()
phone3.record_video(30)
phone3.display_battery()
phone3.power_off()
print("-" * 20)

# Polymorphism in action (treating different smartphone types generically)
def display_device_info(device):
    print(f"Device Info: {device}")
    if isinstance(device, Smartphone):
        device.display_battery()
        if device._is_on:  # Accessing encapsulated attribute (with caution)
            print(f"{device.brand} {device.model} is currently ON.")
        else:
            print(f"{device.brand} {device.model} is currently OFF.")
    print("-" * 20)

display_device_info(phone1)
display_device_info(phone2)
display_device_info(phone3)