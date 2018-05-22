package com.mybatis.dao;

import org.mybatis.cdi.Mapper;
import com.mybatis.model.Student;
import java.util.List;

@Mapper
public interface StudentMapper
{
    void insert(Student student);
    List<Student> selectAll();
}