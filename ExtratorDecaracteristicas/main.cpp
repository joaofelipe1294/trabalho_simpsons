#include "itkImage.h"
#include "itkImageFileReader.h"
#include "itkImageFileWriter.h"
#include "itkRGBToLuminanceImageFilter.h"

#include "ColorExtractor.hpp"
#include "FileHandler.hpp"

#include <iostream>

using namespace std;
using namespace itk;

//const int DIMENSIONS = 2;

typedef Image<unsigned char , DIMENSIONS> GrayscaleImageType;
typedef RGBPixel<unsigned char> RGBPixelType;
typedef Image<RGBPixelType , DIMENSIONS> RGBImageType;
typedef ImageFileReader<RGBImageType> RGBReaderType;
typedef RGBToLuminanceImageFilter<RGBImageType, GrayscaleImageType> GrayscaleFilterType;
typedef ImageFileWriter<GrayscaleImageType> WriterType;
typedef ImageFileWriter<RGBImageType> RGBWriterType;

int main(int argc, char *argv[]){
    
    
/* ------------------------------------ ABRIR IMAGEM ---------------------------------------- */
    
    string dirName = "classes/marge_5/";
    //cout << "DIR : ";
    //cin >> dirName;
    FileHandler* fileHandler = new FileHandler(dirName);
    for (int i = 0; i < fileHandler -> GetNumberOfFiles(); i++) {
        RGBReaderType::Pointer rgbReader = RGBReaderType::New();
        rgbReader -> SetFileName(fileHandler -> GetFiles()[i]);
        RGBImageType::Pointer rgbImage = rgbReader -> GetOutput();
        rgbImage -> Update();
    
/* ---------------------------------------- TEST ------------------------------------------- *
    
    RGBReaderType::Pointer rgbReader = RGBReaderType::New();
    rgbReader -> SetFileName("Train/marge024.bmp");
    RGBImageType::Pointer rgbImage = rgbReader -> GetOutput();
    rgbImage -> Update();
    RGBImageType::IndexType index = {{232 , 12}};
    RGBImageType::PixelType pixel = rgbImage -> GetPixel(index);
    cout << "RED : " << (int) pixel.GetRed() << endl;
    cout << "GREEN : " << (int) pixel.GetGreen() << endl;
    cout << "BLUE : " << (int) pixel.GetBlue() << endl;
    
/* ------------------------------------------------------------------------------------------ */
    
    
/* ------------------------------------ COLOR STATISTICS ------------------------------------ *
    
    int* vetColors = new int[8];
    ColorExtractor* colorExtractor = new ColorExtractor(rgbImage);
    colorExtractor -> GetValues(vetColors);
    
/* ------------------------------------------------------------------------------------------ */
    
/* ------------------------------------- EXTRACT SIMPSON ------------------------------------ */
    
    RGBImageType::RegionType region = rgbImage -> GetLargestPossibleRegion();
    ImageRegionIterator<RGBImageType> imageIterator(rgbImage , region);
    
    while(!imageIterator.IsAtEnd()){
        RGBPixelType pixel = imageIterator.Get();
        int red = (int) pixel.GetRed();
        int green = (int) pixel.GetGreen();
        int blue = (int) pixel.GetBlue();
        if (((red > 232 && red < 250) && (green > 183 && green < 193) && (blue >= 0 && blue < 5)) || ((red > 250 && red <= 255) && (green > 193 && green < 203) && (blue >= 0 && blue < 5)) || ((red > 202 && red <= 255) && (green > 195 && green < 201) && (blue > 30 && blue < 60))) { // amarelo pele
            ++imageIterator;
        }else if ((red > 242 && red < 252) && (green > 94 && green < 104) && (blue > 11 && blue < 21)){ // laranja camiseta bart
            ++imageIterator;
        }else if ((red >= 0 && red < 5) && (green > 3 && green < 13) && (blue > 125 && blue < 135)){ // azul escuro shorts e tenis bart
            ++imageIterator;
        }else if (((red >= 185 && red <= 216) && (green >= 169 && green <= 184) && (blue >= 101 && blue <= 134)) || ((red > 178 && red < 184) && (green > 153 && green < 159) && (blue > 96 && blue < 102))){ // barba homer
            ++imageIterator;
        }else if (((red == 0) && (green > 102 && green < 112) && (blue > 168 && blue < 178)) || ((red > 63 && red < 85) && (green > 96 && green < 118) && (blue > 162 && blue < 184))){ // calca homer
            ++imageIterator;
        }else if (((red > 244 && red <= 255) && (green >= 0 && green < 5) && (blue >= 0 && blue < 5)) || ((red > 189 && red <=255) && (green > 21 && green < 43) && (blue > 5 && blue < 15))){ // vestido lisa e chupeta maggie e acessorios marge
            ++imageIterator;
        }else if (((red >= 0 && red < 5) && (green > 151 && green < 168) && (blue > 217 && blue <= 255)) || ((red > 46 && red < 51) && (green > 129 && green < 143) && (blue > 194 && 217))){ // pijama maggie
            ++imageIterator;
        }else if (((red >= 0 && red < 5) && (green > 61 && green < 71) && (blue > 127 && blue < 137)) || ((red >= 0 && red < 5) && (green > 5 && green < 19) && (blue > 96 && blue < 110))){ // cabelo Marge
            ++imageIterator;
        }else if ((red > 138 && red < 159) && (green > 170 && green < 208) && (blue > 13 && blue < 40)){ // vestido merge
            ++imageIterator;
        }else{
            imageIterator.Set(255);
            ++imageIterator;
        }
        
    }
    
    stringstream imageOut;
    imageOut << "classes/marge_out/" << fileHandler -> GetFiles()[i].substr(dirName.length() , (fileHandler -> GetFiles()[i].length() - dirName.length()));
    cout  << "imageName : " << imageOut.str() << endl;
    RGBWriterType::Pointer rgbWriter = RGBWriterType::New();
    rgbWriter -> SetFileName(imageOut.str());
    rgbWriter -> SetInput(rgbImage);
    rgbWriter -> Update();
    
    }

/* ------------------------------------------------------------------------------------------------ */
    
    /*GrayscaleFilterType::Pointer grayscaleFilter = GrayscaleFilterType::New();
    grayscaleFilter -> SetInput(rgbImage);
    grayscaleFilter -> Update();
    GrayscaleImageType::Pointer grayImage = grayscaleFilter -> GetOutput();
    grayImage -> Update();
    WriterType::Pointer writer = WriterType::New();
    writer -> SetInput(grayImage);
    writer -> SetFileName("gray.bmp");
    writer -> Update();*/
    return EXIT_SUCCESS;
}