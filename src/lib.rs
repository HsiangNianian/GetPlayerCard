use pyo3::prelude::*;
use serde::{Serialize, Deserialize};
use std::collections::HashMap;

#[pyclass]
#[derive(Serialize, Deserialize, Clone)]
pub struct CharacterCard {
    #[pyo3(get, set)]
    pub name: String,
    #[pyo3(get)]
    pub attributes: HashMap<String, u32>,
    #[pyo3(get)]
    pub skills: HashMap<String, u32>,
    #[pyo3(get)]
    pub template: Option<String>,
}

#[pymethods]
impl CharacterCard {
    #[new]
    fn new(name: String) -> Self {
        CharacterCard {
            name,
            attributes: HashMap::new(),
            skills: HashMap::new(),
            template: None,
        }
    }

    fn set_attribute(&mut self, name: String, value: u32) {
        self.attributes.insert(name, value);
    }

    fn set_skill(&mut self, name: String, value: u32) {
        self.skills.insert(name, value);
    }

    fn apply_template(&mut self, template: HashMap<String, Vec<String>>) {
        if let Some(attrs) = template.get("attributes") {
            for attr in attrs {
                self.attributes.entry(attr.clone()).or_insert(0);
            }
        }
        if let Some(skills) = template.get("skills") {
            for skill in skills {
                self.skills.entry(skill.clone()).or_insert(0);
            }
        }
        self.template = template.get("name").and_then(|v| v.get(0).cloned());
    }

    fn to_json(&self) -> String {
        serde_json::to_string(self).unwrap()
    }
}

#[pyfunction]
fn load_template(path: String) -> PyResult<HashMap<String, Vec<String>>> {
    let content = std::fs::read_to_string(path)?;
    Ok(serde_json::from_str(&content).unwrap())
}

#[pymodule]
fn _core(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<CharacterCard>()?;
    m.add_function(wrap_pyfunction!(load_template, m)?)?;
    Ok(())
}