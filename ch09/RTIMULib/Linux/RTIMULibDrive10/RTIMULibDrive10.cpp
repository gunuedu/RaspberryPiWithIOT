////////////////////////////////////////////////////////////////////////////
//
//  This file is part of RTIMULib
//
//  Copyright (c) 2014, richards-tech
//
//  Permission is hereby granted, free of charge, to any person obtaining a copy of
//  this software and associated documentation files (the "Software"), to deal in
//  the Software without restriction, including without limitation the rights to use,
//  copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
//  Software, and to permit persons to whom the Software is furnished to do so,
//  subject to the following conditions:
//
//  The above copyright notice and this permission notice shall be included in all
//  copies or substantial portions of the Software.
//
//  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
//  INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
//  PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
//  HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
//  OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
//  SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


#include "RTIMULib.h"

int main()
{
    int sampleCount = 0;
    int sampleRate = 0;
    uint64_t rateTimer;
    uint64_t displayTimer;
    uint64_t now;

    //  using RTIMULib here allows it to use the .ini file generated by RTIMULibDemo.

    RTIMUSettings *settings = new RTIMUSettings("RTIMULib");

    RTIMU *imu = RTIMU::createIMU(settings);
    RTPressure *pressure = RTPressure::createPressure(settings);

    if ((imu == NULL) || (imu->IMUType() == RTIMU_TYPE_NULL)) {
        printf("No IMU found\n");
        exit(1);
    }

    //  This is an opportunity to manually override any settings before the call IMUInit

    //  set up IMU

    imu->IMUInit();

    //  this is a convenient place to change fusion parameters

    imu->setSlerpPower(0.02);
    imu->setGyroEnable(true);
    imu->setAccelEnable(true);
    imu->setCompassEnable(true);

    //  set up pressure sensor

    if (pressure != NULL)
        pressure->pressureInit();

    //  set up for rate timer

    rateTimer = displayTimer = RTMath::currentUSecsSinceEpoch();

    //  now just process data

    while (1) {
        //  poll at the rate recommended by the IMU

        usleep(imu->IMUGetPollInterval() * 1000);

        while (imu->IMURead()) {
            RTIMU_DATA imuData = imu->getIMUData();

            //  add the pressure data to the structure

            if (pressure != NULL)
                pressure->pressureRead(imuData);

            sampleCount++;

            now = RTMath::currentUSecsSinceEpoch();

            //  display 10 times per second

            if ((now - displayTimer) > 100000) {
                printf("Sample rate %d: %s\n", sampleRate, RTMath::displayDegrees("", imuData.fusionPose));

                if (pressure != NULL) {
                    printf("Pressure: %4.1f, height above sea level: %4.1f, temperature: %4.1f\n",
                           imuData.pressure, RTMath::convertPressureToHeight(imuData.pressure), imuData.temperature);
                }

                fflush(stdout);
                displayTimer = now;
            }

            //  update rate every second

            if ((now - rateTimer) > 1000000) {
                sampleRate = sampleCount;
                sampleCount = 0;
                rateTimer = now;
            }
        }
    }
}

