package com.jpa.entities;

import lombok.Getter;
import lombok.Setter;
import org.apache.johnzon.mapper.JohnzonIgnore;

import javax.persistence.*;
import javax.validation.constraints.NotNull;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlTransient;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

@Getter
@Setter
@Entity
@Table(name="STUDENT")
public class Student implements Serializable
{
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name="ID")
    private Integer id;

    @Column(name="FIRST_NAME")
    private String firstName;

    @Column(name="LAST_NAME")
    private String lastName;

    @Version
    @Column(name="ROW_VERSION")
    private Integer rowVersion;

    @JohnzonIgnore
    @OneToMany(mappedBy = "student")
    private List<Book> bookList = new ArrayList<Book>();

    @Override
    public boolean equals(Object other)
    {
        return (other != null && getClass() == other.getClass() && id != null)
                ? id.equals(((Student) other).id)
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
        return String.format("Student[%d, %s, %s]", id, firstName, lastName);
    }
}
