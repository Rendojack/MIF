package com.mybatis.model;

import lombok.Getter;
import lombok.Setter;
import java.util.List;

@Getter
@Setter
public class Book
{
  private Integer id;
  private String title;
  private String description;
  private Integer studentId;

  // many-to-one
  private Student student;

  // many-to-many
  private List<Author> authorList;

  @Override
  public boolean equals(Object other)
  {
    return (other != null && getClass() == other.getClass() && id != null)
            ? id.equals(((Book) other).id)
            : (other == this);
  }

  @Override
  public int hashCode()
  {
    return (id != null)
            ? (getClass().hashCode() + id.hashCode())
            : super.hashCode();
  }
  @Override
  public String toString()
  {
    return String.format("Book[%d, %s, %s, %d]", id, title, description, studentId);
  }
}
