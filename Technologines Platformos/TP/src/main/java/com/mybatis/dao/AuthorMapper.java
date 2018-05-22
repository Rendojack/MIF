package com.mybatis.dao;

import org.mybatis.cdi.Mapper;
import com.mybatis.model.Author;
import java.util.List;

@Mapper
public interface AuthorMapper
{
    List<Author> selectAll();
}
