//
//  ColorExtractor.cpp
//  ExtratorDeCaracteristicas
//
//  Created by joao lopes on 08/06/16.
//
//

#include "ColorExtractor.hpp"

ColorExtractor::ColorExtractor(RGBImageType::Pointer image){
    this -> image = image;
    this -> bartShirt = 0;
    this -> bartShortsAndShoes = 0;
    this -> homerBeard = 0;
    this -> homerPants = 0;
    this -> lisaDressAndMaggiePacifierAndMargeItems = 0;
    this -> maggiePijamas = 0;
    this -> margeHair = 0;
    this -> margeDress = 0;
    this -> GetData();
}

void ColorExtractor::GetData(){
    RGBImageType::RegionType region = this -> image -> GetLargestPossibleRegion();
    ImageRegionConstIterator<RGBImageType> imageIterator(this -> image , region);
    
    while(!imageIterator.IsAtEnd()){
        RGBPixelType pixel = imageIterator.Get();
        int red = (int) pixel.GetRed();
        int green = (int) pixel.GetGreen();
        int blue = (int) pixel.GetBlue();
        if((red == 247) && (green == 99) && (blue == 16)){ // laranja camiseta bart
            this -> bartShirt++;
        }else if ((red == 0) && (green == 8) && (blue == 132)){ // azul escuro tenis e shorts bart
            this -> bartShortsAndShoes++;
        }else if ((red == 189) && (green == 173) && (blue == 107)){ // barba homer
            this -> homerBeard++;
        }else if ((red == 0) && (green == 107) && (blue == 173)){ // calca homer
            this -> homerPants++;
        }else if ((red == 255) && (green == 0) && (blue == 0)){ // vestido lisa e chupeta maggie e acessorios marge
            this -> lisaDressAndMaggiePacifierAndMargeItems++;
        }else if ((red == 0) && (green == 156) && (blue == 222)){ // pijama maggie
            this -> maggiePijamas++;
        }else if ((red == 0) && (green == 66) && (blue == 132)){ // cabelo Marge
            this -> margeHair++;
        }else if ((red > 138 && red < 160) && (green > 170 && green < 208) && (blue > 20 && blue < 40)){ // vestido merge
            this -> margeDress++;
        }
        ++imageIterator;
    }
    cout << "BART camiseta : " << bartShirt << endl;
    cout << "BART tenis e shots : " << bartShortsAndShoes << endl;
    cout << "HOMER barba : " << homerBeard << endl;
    cout << "HOMER calca : " << homerPants << endl;
    cout << "LISA | MAGGIE | MARGE vestido - chupeta - acessotios : " << lisaDressAndMaggiePacifierAndMargeItems << endl;
    cout << "MAGGIE pijama : " << maggiePijamas << endl;
    cout << "MARGE cabelo : " << margeHair << endl;
    cout << "MARGE vestido : " << margeDress << endl;
}

void ColorExtractor::GetValues(int* values){
    values[0] = this -> bartShirt;
    values[1] = this -> bartShortsAndShoes;
    values[2] = this -> homerBeard;
    values[3] = this -> homerPants;
    values[4] = this -> lisaDressAndMaggiePacifierAndMargeItems;
    values[5] = this -> maggiePijamas;
    values[6] = this -> margeHair;
    values[7] = this -> margeDress;
}