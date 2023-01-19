package com.api.DataAnalysisMeasure.controllers;

import com.api.DataAnalysisMeasure.dtos.DataAnalysisDto;
import com.api.DataAnalysisMeasure.models.DataAnalysisModel;
import com.api.DataAnalysisMeasure.repositories.DataAnalysisRepository;
import com.api.DataAnalysisMeasure.services.DataAnalysisService;
import jakarta.validation.Valid;
import org.apache.catalina.connector.Response;
import org.springframework.beans.BeanUtils;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
@CrossOrigin(origins = "*", maxAge = 3600)
@RequestMapping("/data-analysis")
public class DataAnalysisController {

    final DataAnalysisService dataAnalysisService;

    public DataAnalysisController(DataAnalysisService dataAnalysisService){
        this.dataAnalysisService = dataAnalysisService;
    }

    @GetMapping
    public ResponseEntity<Object> getAllDataAnalysis() {
        return ResponseEntity.status(HttpStatus.OK).body(dataAnalysisService.findAll());
    }

    @PostMapping
    public ResponseEntity<Object> postDataAnalysis(@RequestBody @Valid DataAnalysisDto dataAnalysisDto) {
        var dataAnalysisModel = new DataAnalysisModel();
        BeanUtils.copyProperties(dataAnalysisDto, dataAnalysisModel);
        return ResponseEntity.status(HttpStatus.CREATED).body(dataAnalysisService.save(dataAnalysisModel));
    }

}
