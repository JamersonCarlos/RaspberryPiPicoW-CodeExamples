package com.api.DataAnalysisMeasure.repositories;

import com.api.DataAnalysisMeasure.models.DataAnalysisModel;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import org.yaml.snakeyaml.events.Event;

import java.util.UUID;

@Repository
public interface DataAnalysisRepository extends JpaRepository<DataAnalysisModel, UUID> {

}
