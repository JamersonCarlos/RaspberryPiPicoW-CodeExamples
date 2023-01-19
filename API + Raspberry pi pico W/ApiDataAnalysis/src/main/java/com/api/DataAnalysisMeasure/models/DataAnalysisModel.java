package com.api.DataAnalysisMeasure.models;

import jakarta.persistence.*;

import java.util.UUID;

@Entity
@Table(name = "TB_ANALYSIS_TH")
public class DataAnalysisModel {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private UUID id;

    @Column(nullable = false, length = 10)
    private String temperature;

    @Column(nullable = false, length = 10)
    private String humidity;

    public UUID getId() {
        return id;
    }

    public void setId(UUID id) {
        this.id = id;
    }

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
