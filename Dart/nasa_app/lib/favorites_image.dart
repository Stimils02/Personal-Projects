import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:nasa_app/theme_handler.dart';

class ImageData extends ChangeNotifier {
  List<String> imageurls = [];

  void addImageUrl(String url) {
    if (!imageurls.contains(url)) {
      imageurls.add(url);
      notifyListeners();
    }
  }
}

class FavoriteImages extends StatelessWidget {
  final Map<String, dynamic> image;
  const FavoriteImages({super.key, this.image = const {'url': 'dummy_url'}});

  @override
  Widget build(BuildContext context) {
    ThemeModel model = Provider.of<ThemeModel>(context);
    return Scaffold(
      appBar: AppBar(
        elevation: 0.0,
        backgroundColor: model.backgroundColor,
        title: Center(
          child: Text(
            "Here are the list of images you have browsed through",
            style: TextStyle(color: model.textColor),
          ),
        ),
      ),
      backgroundColor: model.backgroundColor,
      body: Consumer<ImageData>(
        builder: (context, imageData, _) => SingleChildScrollView(
          child: Center(
            child:
                Column(mainAxisAlignment: MainAxisAlignment.center, children: [
              for (var item in imageData.imageurls)
                Image.network(
                  item,
                  fit: BoxFit.cover,
                  height: MediaQuery.of(context).size.height /
                      imageData.imageurls.length,
                ),
            ]),
          ),
        ),
      ),
    );
  }
}
