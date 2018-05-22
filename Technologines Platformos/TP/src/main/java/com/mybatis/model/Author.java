package com.mybatis.model;

import lombok.Getter;
import lombok.Setter;
import java.util.List;

@Getter
@Setter
public class Author
{
    private Integer id;
    private String firstname;
    private String lastName;

    // many-to-many
    private List<Book> bookList;

    public void setFirstName(String firstname)
    {
        this.firstname = firstname;
    }
}
