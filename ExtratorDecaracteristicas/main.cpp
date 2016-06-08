#include "itkImage.h"
#include "itkImageFileReader.h"
#include "itkImageFileWriter.h"
#include "itkRGBToLuminanceImageFilter.h"

#include "ColorExtractor.hpp"

#include <iostream>

using namespace std;
using namespace itk;

//const int DIMENSIONS = 2;

typedef Image<unsigned char , DIMENSIONS> GrayscaleImageType;
typedef RGBPixel<unsigned char> RGBPixelType;
typedef Image<RGBPixelType , DIMENSIONS> RGBImageType;
typedef ImageFileReader<RGBImageType> RGBReaderType;
typedef RGBToLuminanceImageFilter<RGBImageType, GrayscaleImageType> GrayscaleFilterType;






int main(int argc, char *argv[]){

/* ------------------------------------ ABRIR IMAGEM ---------------------------------------- */
    
    RGBReaderType::Pointer rgbReader = RGBReaderType::New();
    rgbReader -> SetFileName("../../../testes_basicos/bart009.bmp");
    RGBImageType::Pointer rgbImage = rgbReader -> GetOutput();
    rgbImage -> Update();
    
    int* vetColors = new int[8];
    ColorExtractor* colorExtractor = new ColorExtractor(rgbImage);
    colorExtractor -> GetValues(vetColors);
    
    
/* ------------------------------------------------------------------------------------------ */

    return EXIT_SUCCESS;
}