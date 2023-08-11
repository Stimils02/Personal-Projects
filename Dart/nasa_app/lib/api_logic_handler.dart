import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:nasa_app/data_storage.dart';
// import 'package:nasa_app/apod_select_page.dart';
// import 'package:flutter_dotenv/flutter_dotenv.dart';

// Good habit always store API Key and secrets file like a .env files
Future<List<dynamic>> getAPOD(double count) async {
  String apiKey = "77D8wvth4JcTKpPrCXBaHlJ2kWGYd6bAnFdb0rpF";
  // await dotenv.load();
  // final variable = dotenv.private_env[]
  int numPictures = count.toInt();
  String numPics = "&count=${numPictures.toString()}";
  // String count = "&count=5";
  String apiUrl = "https://api.nasa.gov/planetary/apod?api_key=$apiKey$numPics";

  // String count = "&count=5";

  final response = await http.get(Uri.parse(apiUrl));

  if (response.statusCode == 200) {
    final body = response.body;
    // print(body);
    if (body.isNotEmpty) {
      // const encoder = JsonEncoder.withIndent(' ');
      // final prettyPrint = encoder.convert(json.decode(body));
      // print(prettyPrint);
      // for (int i = 0; i < decoded.length; i++) {
      //   Map<String, dynamic> = decoded[i];
      // }

      // print(
      //     'Json body length: ${decoded.length}, Json body type: ${decoded.runtimeType}');
      return json.decode(body);
    } else {
      throw Exception("Failed to load SpaceImages");
    }
  } else {
    throw Exception("Failed to load SpaceImages");
  }
}

Future<List<ApodData>> setAPODItems(double count) async {
  List<ApodData> apodDatalist = [];
  try {
    List<dynamic> body = await getAPOD(count);
    for (int i = 0; i < body.length; i++) {
      Map<String, dynamic> temp = body[i];
      ApodData data = ApodData.fromJson(temp);
      apodDatalist.add(data);
    }
    Globals.apodDatalist = apodDatalist;
    Globals.isApodApiCalled = true;
  } catch (e) {
    print("Error: $e");
  }
  return apodDatalist;
}

// Future<void> printAPODItems() async {
//   try {
//     List<ApodData> apodDatalist = await setAPODItems();
//     for (int i = 0; i < apodDatalist.length; i++) {
//       ApodData mymodel = apodDatalist[i];
//       // print(mymodel);
//       // print(
//       //     "Title: ${mymodel.title} Date: ${mymodel.date} url: ${mymodel.url} hdUrl: ${mymodel.hdUrl}");
//       // print("------------------------------------------------");
//     }
//   } catch (e) {
//     print("An error occurred: $e");
//   }
// }

Future<Map<String, dynamic>> getMars(int sol) async {
  String apiKey = "77D8wvth4JcTKpPrCXBaHlJ2kWGYd6bAnFdb0rpF";
  sol.toString();
  String apiUrl =
      "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=$sol&api_key=";

  final response = await http.get(Uri.parse(apiUrl + apiKey));
  if (response.statusCode == 200) {
    final body = response.body;
    if (body.isNotEmpty) {
      // const encoder = JsonEncoder.withIndent(' ');
      // final prettyPrint = encoder.convert(json.decode(body));
      // print(prettyPrint);
      // print(json.decode(body));
      // final decoded = json.decode(body);
      // print(decoded);
      // print(decoded['photos'].length);
      return json.decode(body);
    } else {
      throw Exception("Failed to load Mars Images");
    }
  } else {
    throw Exception("Failed to load Mars Images");
  }
}

Future<List<MarsData>> setMarsItems(double numPictures, double sol) async {
  List<MarsData> marsDataList = [];
  try {
    Map<String, dynamic> body = await getMars(sol.toInt());
    List<dynamic> bodylist = body['photos'];
    for (int i = 0; i < numPictures; i++) {
      Map<String, dynamic> temp = bodylist[i];
      MarsData data = MarsData.fromJson(temp);
      marsDataList.add(data);
    }
    // print(marsDataList);
    Globals.marsDatalist = marsDataList;
    // if (MarsOptions.sol != Globals.currentSol ||
    //     MarsOptions.numPictures != Globals.currNumPics) {
    //   Globals.isMarsApiCalled = false;
    //   Globals.currNumPics = numPictures;
    //   Globals.currentSol = sol;
    //   // print("In the print statement");
    // } else {
    //   Globals.isMarsApiCalled = true;
    //   print("${MarsOptions.sol} ${Globals.currentSol}");
    //   print("Didn't go to print statement");
    // }
  } catch (e) {
    print("Error: $e");
  }
  return marsDataList;
}

// Future<void> printMarsItems(int numPictures, int sol, String camera) async {
//   try {
//     List<MarsData> marsDatalist = await setMarsItems(numPictures, sol, camera);
//     for (int i = 0; i < marsDatalist.length; i++) {
//       MarsData mymodel = marsDatalist[i];
//       print(
//           "Sol: ${mymodel.sol} Camera: ${mymodel.camera} Url: ${mymodel.url} Rover: ${mymodel.roverName}");
//       // const encoder = JsonEncoder.withIndent(' ');
//       // final prettyPrint = encoder.convert(json.decode(bodylist[i]));
//       // print(prettyPrint);
//       print("-------------------------------");
//     }
//   } catch (e) {
//     print("An error occurred: $e");
//   }
// }
