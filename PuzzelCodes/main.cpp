#include <iostream>
#include <random>

#define FILTER_ID			0b110011001100u
#define FILTER_RANDOM		0b001000100010u
#define FILTER_CHECKSUM		0b000100010001u

unsigned genRandom() {
    const unsigned int seed = time(nullptr);
    std::mt19937_64 engine(seed);
    std::uniform_int_distribution<unsigned> random(0, UINT32_MAX);


    return random(engine);
}

unsigned getChecksum(unsigned id, unsigned random) {
    unsigned checksum;
    id &= FILTER_ID;
    random &= FILTER_RANDOM;

    id >>= 2u;
    random >>= 1u;

    checksum = ~(id + random);
    checksum = checksum & FILTER_CHECKSUM;

    return checksum;
}

unsigned encode(unsigned id){
    unsigned random = genRandom() & FILTER_RANDOM;
    unsigned idLower = id & 0b000011u;
    unsigned idMiddle = id & 0b001100u;
    unsigned idUpper = id & 0b110000u;
    unsigned checksum, code;

    std::cout << "ID: " << id << std::endl;
    id = (idUpper << 6u) |  (idMiddle << 4u) | (idLower << 2u);
    checksum = getChecksum(id, random);
    code = id | random | checksum;

    std::cout << "Checksum: " << checksum << std::endl;
    std::cout << "ID code: " << id << std::endl;
    std::cout << "Random: " << random << std::endl;

    return code;
}

unsigned decode(unsigned code) {
    unsigned random = code & FILTER_RANDOM;
    unsigned checksum = code & FILTER_CHECKSUM;
    unsigned id = code & FILTER_ID;
    unsigned checksum_check = getChecksum(id, random);
    unsigned idLower = id &  0b000000001100u;
    unsigned idMiddle = id & 0b000011000000u;
    unsigned idUpper = id &  0b110000000000u;

    std::cout << "Checksum: " << checksum << " : " << checksum_check << std::endl;
    std::cout << "ID code: " << id << std::endl;
    std::cout << "Random: " << random << std::endl;

    id = (idUpper >> 6u) | (idMiddle >> 4u) | (idLower >> 2u);
    std::cout << "ID: " << id << std::endl;

    return checksum_check == checksum ? id : -1;
}

int main()
{
    std::string line;
    unsigned code, id;

    do {
        std::cout << "ID: " << std::flush;
        std::cin >> id;

        code = encode(id);
        std::cout << "Code: " << code << std::endl;

        std::cout << std::endl;
        std::cout << "Input: " << std::flush;
        std::cin >> code;
        int result = decode(code);
        if (result != -1) {
            std::cout << "Game " << result  << " Correct"<< std::endl;
        }
        std::cout << "-----" << std::endl;

    } while (line != "STOP");
    return 0;
}