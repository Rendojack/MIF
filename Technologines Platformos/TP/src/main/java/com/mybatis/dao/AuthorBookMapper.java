package com.mybatis.dao;

import org.mybatis.cdi.Mapper;
import java.util.List;
import com.mybatis.model.AuthorBook;

@Mapper
public interface AuthorBookMapper
{
    List<AuthorBook> selectAll();
}
