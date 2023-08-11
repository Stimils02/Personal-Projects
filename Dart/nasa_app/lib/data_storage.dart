class Globals {
  static bool isApodApiCalled = false;
  static bool isMarsApiCalled = false;
  static List<ApodData> apodDatalist = [];
  static List<MarsData> marsDatalist = [];
}

class MarsOptions {
  static double sol = 0.0;
  static double numPictures = 0.0;
}

class ApodOptions {
  static final List<String> pictureCount = [];
}

class ApodData {
  String title;
  String url;
  String hdUrl;
  String date;

  ApodData({
    this.title = '',
    this.url = '',
    this.hdUrl = '',
    this.date = '',
  });

  factory ApodData.fromJson(Map<String, dynamic> json) {
    return ApodData(
      title: json['title'],
      url: json['url'],
      hdUrl: json['hdurl'],
      date: json['date'],
    );
  }
}

class MarsData {
  int sol;
  String camera;
  String url;
  String roverName;

  MarsData({
    this.sol = 1,
    this.camera = '',
    this.url = '',
    this.roverName = '',
  });

  factory MarsData.fromJson(Map<String, dynamic> json) {
    return MarsData(
      sol: json['sol'],
      camera: json['camera']['name'],
      url: json['img_src'],
      roverName: json['rover']['name'],
    );
  }
}
