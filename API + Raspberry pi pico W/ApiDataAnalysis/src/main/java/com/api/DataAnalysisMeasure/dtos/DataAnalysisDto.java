package com.api.DataAnalysisMeasure.dtos;


import jakarta.validation.constraints.NotBlank;

public class DataAnalysisDto {

    @NotBlank
    private String temperature;

    @NotBlank
    private String humidity;

    public String getTemperature() {
        return temperature;
    }

    public void setTemperature(String temperature) {
        this.temperature = temperature;
    }

    public String getHumidity() {
        return humidity;
    }

    public void setHumidity(String humidity) {
        this.humidity = humidity;
    }
}
