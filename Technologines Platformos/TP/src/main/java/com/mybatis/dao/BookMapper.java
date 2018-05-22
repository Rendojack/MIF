package com.mybatis.dao;

import org.mybatis.cdi.Mapper;
import java.util.List;
import com.mybatis.model.Book;

@Mapper
public interface BookMapper
{
    void insert(Book book);
    void update(Book book);
    List<Book> selectAll();
}
