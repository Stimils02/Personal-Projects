import 'package:flutter/material.dart';
import 'package:nasa_app/mars_select_page.dart';
import 'package:nasa_app/theme_handler.dart';
import 'package:provider/provider.dart';
import 'package:nasa_app/apod_select_page.dart';

class ExploreAPI extends StatelessWidget {
  const ExploreAPI({super.key});

  @override
  Widget build(BuildContext context) {
    ThemeModel model = Provider.of<ThemeModel>(context);
    return Scaffold(
      appBar: AppBar(
        elevation: 0.0,
        backgroundColor: model.backgroundColor,
        title: Row(
          mainAxisAlignment: MainAxisAlignment.spaceAround,
          children: [
            Text(
              "Get Astronomy Pictures",
              style: TextStyle(color: model.textColor),
            ),
            Text(
              "Get Mars Pictures",
              style: TextStyle(color: model.textColor),
            ),
          ],
        ),
      ),
      backgroundColor: model.backgroundColor,
      body: Column(
        children: [
          Expanded(
            child: Row(
              children: [
                Expanded(
                  child: Center(
                    child: InkWell(
                      onTap: () {
                        Navigator.of(context).push(
                          MaterialPageRoute(
                            builder: (_) => const SelectApodMenu(),
                          ),
                        );
                        // Globals.isApodApiCalled = true;
                      },
                      child: Container(
                        decoration: const BoxDecoration(
                          image: DecorationImage(
                            image: AssetImage('images/Galaxy.jpg'),
                            fit: BoxFit.fitHeight,
                          ),
                        ),
                        // child: Stack(
                        //   children: [
                        //     Positioned(
                        //       bottom: 0,
                        //       left: 120,
                        //       right: 0,
                        //       child: Text(
                        //         "Get Astronomy Images",
                        //         style: TextStyle(
                        //           fontSize: 12,
                        //           color: model.textColor,
                        //         ),
                        //       ),
                        //     ),
                        //   ],
                        // ),
                      ),
                    ),
                  ),
                ),
                Expanded(
                  child: Center(
                    child: InkWell(
                      onTap: () {
                        Navigator.of(context).push(
                          MaterialPageRoute(
                            builder: (_) => const SelectMarsMenu(),
                          ),
                        );
                      },
                      child: Container(
                        decoration: const BoxDecoration(
                          image: DecorationImage(
                              image: AssetImage('images/Mars.jpg'),
                              fit: BoxFit.fitHeight),
                        ),
                        // child: Stack(
                        //   children: [
                        //     Positioned(
                        //       bottom: 0,
                        //       left: 0,
                        //       right: 0,
                        //       // top: 190,
                        //       child: Text(
                        //         "Get Mars Images",
                        //         style: TextStyle(
                        //           fontSize: 12,
                        //           color: model.textColor,
                        //         ),
                        //         textAlign: TextAlign.center,
                        //       ),
                        //     ),
                        //   ],
                        // ),
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
