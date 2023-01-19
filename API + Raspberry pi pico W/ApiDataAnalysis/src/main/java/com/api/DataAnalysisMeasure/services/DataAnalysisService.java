package com.api.DataAnalysisMeasure.services;

import com.api.DataAnalysisMeasure.dtos.DataAnalysisDto;
import com.api.DataAnalysisMeasure.models.DataAnalysisModel;
import com.api.DataAnalysisMeasure.repositories.DataAnalysisRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
public class DataAnalysisService {
    final DataAnalysisRepository dataAnalysisRepository;

    public DataAnalysisService(DataAnalysisRepository dataAnalysisRepository){
        this.dataAnalysisRepository = dataAnalysisRepository;
    }

    public List<DataAnalysisModel> findAll() {
        return this.dataAnalysisRepository.findAll();
    }

    @Transactional
    public DataAnalysisModel save(DataAnalysisModel dataAnalysisModel) {
        return this.dataAnalysisRepository.save(dataAnalysisModel);
    }

}
